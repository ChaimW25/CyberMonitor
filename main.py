import cmd
import platform
import subprocess
import os
import time
from os.path import exists
import psutil
from datetime import datetime
import re
SERCIVE_LIST = "serviceList.log"
STATUS_LOG = "Status_Log.log"
serviceDict = {}
# def is_service_running(name):
#     with open(os.devnull, 'wb') as hide_output:
#         exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
#         print(exit_code)
#         return exit_code == 0

def linux():

    os.system("date +%Y-%m-%d,%H:%M:%S >> {}".format(SERCIVE_LIST))
    status = os.system("service --status-all | grep + >> {}".format(SERCIVE_LIST))
    print(status)


def windows():
 file=open(SERCIVE_LIST, 'a')
 file1=open(STATUS_LOG, 'a')
 now=datetime.now()
 currTime=now.strftime("%Y-%m-%d %H:%M:%S")
 print("\nThe time and date: {} \n".format(currTime))
 file.write("The time and date: {} \n".format(currTime))
 for service in psutil.win_service_iter():
  service_name = service.name()
  print(service_name)
  service_status = service.status()
  if serviceDict.get(service_name)==None:
      s = "new service:" + service_name
      file1.write(s + "\n")
  else:
      sta = serviceDict[service_name]
      if service_status != sta:
          s = service_status + service_name
          file1.write(s + "\n")
  serviceDict[service_name] = service_status
  if service.status()== "running":
     # s = service_name+ "   |   " + service_status
     file.write( service_name +"\n")
     print(service_status)
     service_description = service.description()
     print(service_description)
     print("            ")


if _name_ == '_main_':
 status = platform.system() # print if window or linux
 print(status)

 if exists(SERCIVE_LIST):
    os.remove(SERCIVE_LIST)
 file = open(SERCIVE_LIST, 'a')
 if exists(STATUS_LOG):
    os.remove(STATUS_LOG)
 file = open(STATUS_LOG, 'a')

 timeUnit = input("Please enter a time unit in seconds: ")
 timeUnit = int(timeUnit)
 while True:
     if (status == "Windows"):
        windows()
     else:
         linux()
     time.sleep(timeUnit)