import difflib
import platform
import subprocess
import os
import time
from os.path import exists
import psutil
from datetime import datetime

from monitor import monitor

SERCIVE_LIST = "serviceList.log"
DATES = "date.txt"

class manualMonitor:
    def __init__(self, monitor):
        self.mon=monitor


    file1 = open(SERCIVE_LIST, 'r')
    lines1 = file1.readlines()

    file2=open(DATES,'r')
    lines2 = file1.readlines()

    now = datetime.now()
    currTime = now.strftime("%Y-%m-%d %H:%M:%S")
    strtDate = input("Please enter start time in this format '22-03-25 12:35:14' : ")
    endDate = input("Please enter end time in this format: '22-03-25 12:35:14' : ")

    times=[]
    times.append("0")
    i=1
    dateObj=[]
    for line in lines2:
        times.append(line.split('~'))
        dateObj.append(datetime.strptime(times[2*i-1], '%y-%m-%d,%H:%M:%S'))
        i+=1

    strtDate=datetime.strptime(strtDate, '%m/%d/%y,%H:%M:%S')
    endDate=datetime.strptime(endDate, '%y-%m-%d,%H:%M:%S')

    i=1
    for date in dateObj:
        if strtDate<date:
            strtTime=i*2
            break
    for date in dateObj:
        if endDate<date:
            endTime=i*2
            break

    with open('file1.txt') as file_1:
        file_1_text = file_1.readlines()

    with open('file2.txt') as file_2:
        file_2_text = file_2.readlines()

    # Find and print the diff:
    for line in difflib.unified_diff(file_1_text, file_2_text, fromfile='serviceList.log',
            tofile='serviceList.log', lineterm=''):
        print(line)

if __name__ == '__main__':
    m= monitor
    mm=manualMonitor(m)
    manualMonitor()

# 2022-03-25 12:35:56
# 2022-03-25 12:35:59