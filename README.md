# todoist2csv

### Background

I wanted to use Todoist for tracking my daily habits as 
* it has a simple widget I can add to my phone's homescreen,
* it has an easy way to categorize tasks into categories and labels, and
* I already use it for managing tasks for some of my projects.


IFTTT allows me to connect to Todoist and track when a task that has a specific label (in my case ```daily_habits```) has been completed. This would allow me to keep track of the date and time of completion of habits in a spreadsheet, where I can later analyze and visualize the data.

### Problem

IFTTT's ```Add row to spreadsheet``` function outputs in an unhelpful format for storing the data in a clear manner and analyzing them. For example, if you select the date and time of completion as well as the task name to be added each time as a row to the spreadsheet, the spreadsheet would start looking like this:

```
June 3, 2021 at 02:20PM	Running
June 3, 2021 at 09:04PM	Meditating
June 4, 2021 at 08:25PM	Running
June 5, 2021 at 09:40PM	Sleeping Early
```

which could be a pain to turn into a useful visualization like this: 

![Image of Calendar Visualization](https://github.com/chrispla/todoist2csv/blob/main/sample_visualization.png)

Furthermore, some of my days end after midnight, which would normally mess the system up.

### This script

This script reads a .csv with the IFTTT output format and exports a .csv with the habits as a header, the dates on as the first column, and a binary value to indicate whether each task has been completed, as can be seen below. 


| Date | Running | Meditating | Sleeping Early | 
| --- | --- | --- | --- |
| 2021-06-03 | 1 | 1 | 0 | 
| 2021-06-04 | 1 | 0 | 0 |
| 2021-06-05 | 0 | 0 | 1 |

At the moment, you have to edit the script and enter the habit names and their index, which defines the order they are printed. You also have to edit the script to specify the input and output .csv files. The boundary time for the start of a new day is set to 5:00AM.

### Future work

When I find more time, I'll change the input/output directories, the list of habits, as well as the day change time to be read through terminal input.




