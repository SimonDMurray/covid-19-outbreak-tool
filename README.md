![Python application](https://github.com/ARU-Bioinf-ISE/covid19-graphs-SimonDMurray/workflows/Python%20application/badge.svg)
# A tool to download and plot Covid-19 disease outbreak data

Please see [README_instructions.md](README_instructions.md)


## Installing the `covid19_graphs` package (for developers)

To install the `covid19_graphs` package first git clone this repo
then 
```
cd REPO_DIR
pip install -e . 
```
To test your installation run the `covid19_graphs` command line script.
```
covid19_graphs -h
```
You should get an output like
```
$ covid19_graphs -h
usage: covid19_graphs [-h] [-d] OUT_DIR

tool to download and process COVID-19 data

positional arguments:
  OUT_DIR      directory for output files

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  turn on debug message logging output
```

# Instructions for using covid-19 package
1) Make sure you are in the directory you want the output directory to be placed within
2) Run the command ```covid19_graphs output_directory``` where output_directory is what you
    want the output directory to be.
3) Inside your current directory and new directory will be produced with the data inside.
    The data will be named ConfirmedCases, Deaths, Recovered. The .csv files are the data 
    and the .png are the graphs.
4) The daily new data is also in output file. They are called ConfirmedCases_daily_new_cases,
    Deaths_daily_new_cases, Recovered_daily_new_cases. The .csv files are the data and the 
    .png files are the graphs. 
5) If the user does not want to run the script then they can go to https://simondmurray.github.io/
    which is where I automatically upload the data to.
6) The daily report data is in a line graph rather than a bar graph so that each regions new daily cases can be compared. I       feel this is more useful as it can show how different regions are being affected daily, rather than the world as a whole       (which will not be representative for each individual region).  

# Explanation of Automation
In order to get the automation working I looked into a software called CRON.
I created a file known as a crontab and used the CRON notation to specify how
regularly I wanted the crontab to run. I then specified which file I wanted
the crontab to execute. I told the crontab to execute a bash script called run
(bash script contents are displayed in README_manual_tests). The bash script
contained all the commands I need to be executed daily in order to have the 
package automated. I also had to specify the correct paths and environments
in order to have the right versions of all packages installed.

# Manuel Testing Evidence

## All data I used is available [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).

## Graphs
### In order to test whether the plotting in my script worked I had to analyse the graphs
### and see if they were the correct format, style and that the data looked correct
#### This is the image produced by my script of the number of confirmed cases of coronavirus by date
![ConfirmedCases Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/ConfirmedCases.png?raw=true)

#### This is the image produced by my script of the number of deaths by coronavirus by date
![Deaths Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Deaths.png?raw=true)

#### This is the image produced by my package of the number of recoveries from coronavirus by date
![Recovered Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Recovered.png?raw=true)

These graphs all have appropriate title, scale and legend. The dates are the english way 
and there are different plots for different locations. 

The directory these images are placed in for easy access for users is:
```
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/output
``` 
The final directory is placed inside the working directory which the user runs the package
and is named after the input the user provides when they run the script.

The graphs are also placed in the directory:
```
/Users/sm42/University/2019.20/SoftwareDev/coursework/SimonDMurray.github.io/data
```
This directory is then uploaded to github pages and the images are displayed on
[this webpage](https://simondmurray.github.io/).

## CSVs
#### Here are the links to the 3 CSVs my package produces:
[Confirmed Cases CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/ConfirmedCases.csv)

[Death CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Deaths.csv)

[Recovered CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Recovered.csv)

3 CSVs are produced, one from each set of data available on the John Hopkins website. They are saved
in the same format and order as available online. 

The directory these CSVs are in for easy user access:
```
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/output
``` 
The final directory is placed inside the working directory which the user runs the package
and is named after the input the user provides when they run the script. 

The CSVs are also placed in the directory:
```
/Users/sm42/University/2019.20/SoftwareDev/coursework/SimonDMurray.github.io/data
```
This directory is then uploaded to github pages and the CSVs are available on
[this webpage](https://simondmurray.github.io/).

## Testing
I have 8 unit tests available in the directory:
```
/Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs/tests
```
All tests are passed as evidenced:
```
=========================================================================================================================== test session starts ============================================================================================================================
platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.12.0
rootdir: /Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray
collected 11 items                                                                                                                                                                                                                                                         

test_covid19processing.py .......                                                                                                                                                                                                                                    [ 63%]
test_parse_command_line_args.py ....                                                                                                                                                                                                                                 [100%]

============================================================================================================================ 11 passed in 3.66s ============================================================================================================================
```

## Automation
I use CRON to automate the process so that the user does not even need to run the script if needed.
```
USER=sm42
HOME=/home/sm42
SHELL=/bin/bash
PATH=/Users/sm42/Sanger/minconda3/bin:/usr/bin:$PATH
0 9 * * * /Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/run
```
The crontab shown above sets the right set of environment variables in order for script to work.
The crontab runs the following bash script, every minute while computer is on:
```
#!/bin/bash
source /Users/sm42/Sanger/miniconda3/bin/activate covid19
cd /Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/
/Users/sm42/Sanger/miniconda3/envs/covid19/bin/pytest /Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/covid19_graphs/tests/*.py
/Users/sm42/Sanger/miniconda3/envs/covid19/bin/python /Users/sm42/University/2019.20/SoftwareDev/coursework/covid19-graphs-SimonDMurray/deployment_script.py
covid19_graphs output
/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m 'CRON Automatic Git Commit'
/usr/bin/git push
cd /Users/sm42/University/2019.20/SoftwareDev/coursework/SimonDMurray.github.io
/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m 'CRON Automatic Git Commit'
/usr/bin/git push
```
This shows that the script activates the right environment where all the dependencies are store.
It then sets up the data folder read for github pages deployment.
It then runs the script using correct python version.
The script finally updates the github pages repository with new data (if the data has been updated)

## Daily New Cases

The daily new cases data was also implemented and all that data can be found by the following links.

[Daily Confirmed Cases CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/ConfirmedCases_daily_new_cases.csv)

[Daily Death CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Deaths_daily_new_cases.csv)

[Daily Recovered CSV](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Recovered_daily_new_cases.csv)

![Daily ConfirmedCases Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/ConfirmedCases_daily_new_cases.png?raw=true)

#### This is the image produced by my script of the number of deaths by coronavirus by date
![Daily Deaths Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Deaths_daily_new_cases.png?raw=true)

#### This is the image produced by my package of the number of recoveries from coronavirus by date
![Daily Recovered Graph](
https://github.com/SimonDMurray/SimonDMurray.github.io/blob/master/data/Recovered_daily_new_cases.png?raw=true)