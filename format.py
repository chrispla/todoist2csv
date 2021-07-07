import argparse
import csv
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np

# Argument parser
parser = argparse.ArgumentParser(description="Define input and output paths.")
parser.add_argument("--input_path",
                    required=True,
                    help='path of IFTTT csv file')
parser.add_argument("--output_path",
                    default=Path.cwd()/"output.csv",
                    help="output path (directory and name), "
                         "default outputs to cwd")
args = parser.parse_args()
input_path = args.input_path
output_path = args.output_path

# Load data into list of [Date, Habit name]
with open(input_path, "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# Get all unique habit names
habits = list(set(row[1] for row in data))

# IFTTT Datetime format
dt_format = "%B %d, %Y at %I:%M%p"
# Get start and end datetimes for data
start_dt = datetime.strptime(data[0][0], dt_format)
end_dt = datetime.strptime(data[-1][0], dt_format)
# Calculate number of days in range
day_no = (end_dt - start_dt).days + 2
# Create date list
dates = [start_dt+timedelta(days=i) for i in range(day_no)]

# Create output array (extra space for header and date column)
X = np.zeros((day_no+1, len(habits)+1), dtype='object')
X[0, 0] = ''  # empty first cell
# Add header
X[0, 1:] = np.asarray(habits)
# Populate date column with dates formated as dd/mm/yyyy
X[1:, 0] = np.asarray([date.strftime("%d/%m/%Y") for date in dates])

# Fill habit entries
d_ptr = 0  # pointer for list of dates
for row in data:  # go through data and match dates
    row_datetime = datetime.strptime(row[0], dt_format)
    # move pointer until the correct date is found
    while row_datetime.date() != dates[d_ptr].date():
        d_ptr += 1
    # when correct date is found, change cell for row's date and habit to 1
    X[d_ptr+1, habits.index(row[1])+1] = '1'

# Write to .csv
np.savetxt(output_path, X, fmt='%s', delimiter=';')
