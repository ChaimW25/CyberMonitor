import platform
import subprocess
import os
import time
from os.path import exists
import psutil
from datetime import datetime

SERCIVE_LIST = "serviceList.log"
DATES = "date.txt"

file = open(SERCIVE_LIST, 'a')
file=open(DATES,'a')

now = datetime.now()
currTime = now.strftime("%Y-%m-%d %H:%M:%S")
strtDate = input("Please enter start time")
endDate = input("Please enter end time")

times=[]
times.append("0")
i=1
dateObj=[]
for line in DATES:
    times.append(line.split('~'))
    dateObj.append(datetime.strptime(times[2*i-1], '%y-%m-%d,%H:%M:%S'))
    i+=1

strtDate=datetime.strptime(strtDate, '%y-%m-%d,%H:%M:%S')
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

    # //now we got in strtTime the line of the startTime monitor in serviceList.log
    # //and in endTime the line of the endTime in serviceList.log
    # //we just need to compare between the both row by row (sort by alpha bet) with pointers

