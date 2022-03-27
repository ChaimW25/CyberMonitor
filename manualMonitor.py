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
serviceDict1={}
serviceDict2={}


class manualMonitor:
    def __init__(self, monitor):
        self.mon=monitor


    file1 = open(SERCIVE_LIST, 'r')
    lines1 = file1.readlines()
    #reading the help file that helps us to save the dates in the "serviceList.log" file
    file2=open(DATES,'r')
    lines2 = file1.readlines()
    #getting the times from the user as inputs
    now = datetime.now()
    currTime = now.strftime("%Y-%m-%d %H:%M:%S")
    strtDate = input("Please enter start time in this format '2022-03-25 12:35:14' : ")
    endDate = input("Please enter end time in this format: '2022-03-25 12:35:14' : ")

    #using times[]-save the dates and their pos in the file,
    # dateObj[]-  save the dates
    times=[]
    times.append("0")
    i=1
    dateObj=[]
    #appending all the dates into a list
    for line in lines2:
        times.append(line.split('~'))
        dateObj.append(datetime.strptime(times[2*i-1], '%y-%m-%d %H:%M:%S'))
        i+=1
    #convert the input daes to our format-not necessary
    strtDate=datetime.strptime(strtDate, '%y-%m-%d %H:%M:%S')
    endDate=datetime.strptime(endDate, '%y-%m-%d %H:%M:%S')

    i=1
    #saving the user first time- start and end index pos range in the file
    for date in dateObj:
        if strtDate>date:
            strtTime=i*2
            strtTime2=(i+1)*2
            break
        i+=1
    # doing the same with the user second time
    for date in dateObj:
        if endDate>date:
            endTime=i*2
            endTime2=(i+1)*2
            break
        i+=1

    #reading the file in the first time range and insert the sevices names into dict keys
    fileA=open(SERCIVE_LIST, 'r')
    posA=fileA.seek(times[strtTime],times[strtTime])
    for line in fileA:
        while pos < times[strtTime2]:
            serviceDict1[line] = "is running"
            pos = fileA.tell()
    #doing the same with the second time
    posA=fileA.seek(times[endTime],times[endTime])
    for line in fileA:
        while pos < times[endTime2]:
            serviceDict2[line] = "is running"
            pos = fileA.tell()

    #print the changes between the first time and second time
    str=""
    for key in serviceDict1:
        if serviceDict2.get(key) == None:
            str += "The service {} stopped" .format(key)
    for key in serviceDict2:
        if serviceDict1.get(key)==None:
            str += "The service {} begin" .format(key)
    print(str)


    # fileB=open(SERCIVE_LIST, 'r')
    # posB=fileB.seek(endTime,endTime)


    # with open('serviceList.log') as file_1:
    #     file_1_text = file_1.readlines()
    #
    # with open('serviceList.log') as file_2:
    #     file_2_text = file_2.readlines()
    #
    # # Find and print the diff:
    # for line in difflib.unified_diff(file_1_text, file_2_text, fromfile='serviceList.log',
    #         tofile='serviceList.log', lineterm=''):
    #         print(line)

if __name__ == '__main__':
    m= monitor
    mm=manualMonitor(m)
    # manualMonitor()

# 22-03-25 12:35:56
# 2022-03-25 12:35:59