import csv
from datetime import datetime as dt
from datetime import timedelta as td

# Habits to read and output in correct order
habits = {"EXE":1, "MAS":2, "MED":3, "DEN":4, "MOI":5, "COM":6, "SD7":7, "PHY":8}
habit_no = len(habits)
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

formatted = [] # all new data
# list with zero entries for habits
habit_entries = []
for i in range(habit_no):
    habit_entries.append('0')
temp_max = first_max
# create list of sucessive dates, followed by '0' entries for habits
while temp_max <= last_max:
    formatted.append([temp_max] + habit_entries)
    temp_max = temp_max + td(days = 1)

# for every date, check if there are any entries and add them
for i, row in enumerate(formatted):
    # #debug
    # print("Date checked:", row[0])
    entries_added = 0
    for j, entry in enumerate(data):
        #check if date of entry is smaller
        if dt.strptime(entry[0], dt_format) < row[0]:
            # #debug
            # print(dt.strptime(entry[0], dt_format), "is smaller.")
            formatted[i][habits[entry[1]]] = 1 #retrieve habit index from dictionary
            entries_added += 1
        else:
            # #debug
            # print(dt.strptime(entry[0], dt_format), "isn't smaller.")
            #remove added entries from original list because only one sided date check is done
            for k in range(entries_added):
                # #debug
                # print("Removed", data[0])
                data.pop(0)
            break

# #debug
# print(formatted) 

# Write reformatted data to csv
with open("/Users/chris/Google Drive/Habit Tracking/out.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['Date'] + list(habits.keys())) #prepend header
    writer.writerows(formatted)



        