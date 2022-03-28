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

    def start(self,strtDate,endDate):
     file1 = open(SERCIVE_LIST, 'r')
     lines1 = file1.readlines()
     #reading the help file that helps us to save the dates in the "serviceList.log" file
     file2=open(DATES,'r')
     lines2 = file2.readlines()
     #getting the times from the user as inputs
     now = datetime.now()
     currTime = now.strftime("%d/%m/%Y %H:%M:%S")
     # strtDate = input("Please enter start time in this format '2022-03-25 12:35:14' : ")
     # endDate = input("Please enter end time in this format: '2022-03-25 12:35:14' : ")

     #using times[]-save the dates and their pos in the file,
     # dateObj[]-  save the dates
     times=[]
     times.append("0")
     i=1
     dateObj=[]
     #appending all the dates into a list
     for line in lines2:
        times.append(line.split('~'))
        # print(times)
        # print(times[2*1-1])
        datetime1=times[2*1-1][0]
        # print(datetime1)
        dateObj.append(datetime.strptime(datetime1, "%Y/%d/%m %H:%M:%S"))
        i+=1
     #convert the input daes to our format-not necessary
     strtDate=datetime.strptime(strtDate, "%d/%m/%Y %H:%M:%S")
     endDate=datetime.strptime(endDate, "%d/%m/%Y %H:%M:%S")

     i=1
     #saving the user first time- start and end index pos range in the file
     strtTime=1
     strtTime2=2
     endTime=1
     endTime2=2
     for date in dateObj:
        if strtDate>date:
            # strtTime=i*2
            strtTime=i
            # strtTime2=(i+1)*2
            strtTime2=i+1
            break
        i+=1
     # doing the same with the user second time
     for date in dateObj:
        if endDate>date:
            # endTime=i*2
            endTime=i
            endTime2=i+1
            # endTime2=(i+1)*2
            if i==len(times):
             endTime=i-1
             endTime2=len(lines1)-1
            break
        i+=1

     #reading the file in the first time range and insert the sevices names into dict keys
     fileA=open(SERCIVE_LIST, 'r')
     lines = fileA.readlines()
     # posA=int(fileA.seek(int(times[strtTime][1]),int(times[strtTime][1])))
     # for line in fileA:
     posA = int(times[strtTime][1])+1
     posB = int(times[strtTime2][1])
     while posA < posB:
            serviceDict1[lines[posA]] = "is running"
            # posA = fileA.tell()
            posA=posA+1
     #doing the same with the second time
     posA = int(times[endTime][1])+1
     if endTime2 <len(times):
         endTime2=int(times[endTime2][1])
     else:
         endTime2=endTime2+1
     while posA < (endTime2):
            serviceDict2[lines[posA]] = "is running"
            # posA = fileA.tell()
            posA=posA+1
     # # posA=fileA.seek(int(times[endTime]),int(times[endTime]))
     # for line in fileA:
     #    while posA < int(times[endTime2]):
     #        serviceDict2[line] = "is running"
     #        posA = fileA.tell()

     #print the changes between the first time and second time
     str=""
     print(serviceDict2)
     print(serviceDict1)

     for key in serviceDict1:
        if serviceDict2.get(key) == None:
            str += "The service {} stopped".format(key[0:(len(key)-1)])
     for key in serviceDict2:
        if serviceDict1.get(key)==None:
            str += "The service {} begin".format(key[0:(len(key)-1)])
     print(str)
     return str


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
    s1="2022/03/27 19:55:54"
    s2="2022/03/27 19:57:00"
    m= monitor
    mm=manualMonitor(m)
    mm.start(s1,s2)
    # manualMonitor()

# 22-03-25 12:35:56
# 2022-03-25 12:35:59