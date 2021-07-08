### Background

I wanted to use Todoist for tracking my daily habits as 
* it has a simple widget I can add to my phone's homescreen,
* it has an easy way to categorize tasks into categories and labels, and
* I already use it for managing tasks for some of my projects.

The problem is that I want to be keeping a record of my completed habits so that I can later analyze and visualize them, and, just like many actual habit tracking apps, keeping the records in a sheet is either impossible or very cumbersome.

I found that the IFTTT applet [Todoist task to Google Sheets](https://ifttt.com/applets/EZjYdmik) allows me to connect to Todoist and track when a task with a specific label (in my case ```daily_habits```) has been completed. This would allow me to keep track of the date and time of completion of habits in a spreadsheet, where I can later analyze and visualize the data.

### Problem

The ```Add row to spreadsheet``` function of the IFTTT applet outputs in an unhelpful format for storing the data in a clear manner and analyzing them. For example, if you select the date and time of completion as well as the task name to be added each time as a row to the spreadsheet, the spreadsheet would start looking like this:

```
June 3, 2021 at 07:20AM	Running
June 3, 2021 at 08:04AM	Meditating
June 4, 2021 at 08:25PM	Running
June 5, 2021 at 09:40PM	Sleeping Early
```

which could be a pain to turn into a useful visualization like this: 

![Image of Calendar Visualization](https://github.com/chrispla/todoist2csv/blob/main/sample_visualization.png)

### This script

This script reads a csv with the IFTTT output format and exports a csv with the habits as a header, the dates as the first (0th) column, and a binary value to indicate whether each task has been completed, as can be seen below. 


| Date | Running | Meditating | Sleeping Early | 
| --- | --- | --- | --- |
| 03/06/2021 | 1 | 1 | 0 | 
| 04/06/2021 | 1 | 0 | 0 |
| 05/06/2021 | 0 | 0 | 1 |

### Instructions

You can run this script with python 3 using the arguments --input_path to define the path of the IFTTT csv file, and, optionally, --output_path to define the directory and name of the formatted csv (see example below). If no output path is defined, the file ``output.csv`` is generated in the current working directory.
```python3
python3 format.py --input_path=/Users/chris/IFTTThabits.csv --output_path=/Users/chris/habits.csv
```

You'll need python 3 as well as the python modules 
* ``argparse`` to parse command line arguments;
* ``pathlib`` to manage the given paths;
* ``datetime`` for datetime parsing and operations; and 
* ``numpy`` for creating the output table.

For instructions on how to install python modules, check the [python docs](https://docs.python.org/3/installing/index.html).



