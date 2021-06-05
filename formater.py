import csv
from datetime import datetime as dt
from datetime import timedelta as td

# Habits to read and output in correct order
habits = ["EXE", "MAS", "MED", "DEN", "MOI", "COM", "DS7", "PHY"]
# Spreadsheet to read
filepath = '/Users/chris/Google Drive/Habit Tracking/2-day rules IFTTT.csv'
# Datetime format
dt_format = "%B %d, %Y at %I:%M%p"

# load data into list of rows (lists)
with open(filepath, "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# get datetime boundary for first and last date
first_max = dt.strptime(data[0][0], dt_format)
if int(first_max.strftime("%H"))<5: # if before 5AM, belongs to previous day
    first_max = first_max.replace(hour=5, minute=0, second=0, microsecond=0) #set to day boundary
else: #if after 5AM, belongs to current date
    first_max = first_max + td(days = 1) #shift forward one day
    first_max = first_max.replace(hour=5, minute=0, second=0, microsecond=0) #set to day boundary

last_max = dt.strptime(data[-1][0], dt_format)
if int(last_max.strftime("%H"))<5: # if before 5AM, belongs to previous day
    last_max = last_max.replace(hour=5, minute=0, second=0, microsecond=0) #set to day boundary
else: #if after 5AM, belongs to current date
    last_max = last_max + td(days = 1) #shift forward one day
    last_max = last_max.replace(hour=5, minute=0, second=0, microsecond=0) #set to day boundary

print('First date boundary: ', first_max)
print('Last date boundary: ', last_max)

# create list of sucessive dates, followed by '0' entries for habits

        