import platform
import os
import time
from os.path import exists
import psutil
from datetime import datetime
import hashlib


SERCIVE_LIST = "serviceList.log"
STATUS_LOG = "Status_Log.log"
serviceDict = {}
TEMP = "temp.txt"
DATES = "date.txt"




class monitor:

    def __init__(self,slist=None, wo=None, stop=None,location=0):
        self.location=location
        self.slist = []
        self.stop = False
        self.wo = []
        if exists(SERCIVE_LIST):
            os.remove(SERCIVE_LIST)
        # file = open(SERCIVE_LIST, 'a')
        if exists(STATUS_LOG):
            os.remove(STATUS_LOG)
        # file = open(STATUS_LOG, 'a')

    def linux(self):
        file = open(SERCIVE_LIST, 'a')
        file2 = open(DATES, 'a')
        date_location = file.tell()
        now = datetime.now()
        currTime = now.strftime("%Y/%m/%d %H:%M:%S")
        sl = currTime + "~" + str(date_location)
        file2.write(sl + "\n")
        file.write("The time and date: ")
        os.system("date +%Y/%m/%d,%H:%M:%S >> {}".format(SERCIVE_LIST))
        status = os.system("service --status-all | grep + >> {}".format(SERCIVE_LIST))
        file1 = open(STATUS_LOG, 'a')
        os.system("service --status-all >> {}".format(TEMP))
        with open(TEMP) as file:
         for line in file:
            size1 = line.find("[", 1)
            service_status = "running" if line[size1 + 2] == '+' else "stopped"
            service_name = line[size1 + 7:len(line) - 1]
            if serviceDict.get(service_name) == None:
                s = "new service:" + service_name
                file1.write(s + "\n")
                self.slist.append(s)
            else:
                sta = serviceDict[service_name]
                if service_status != sta:
                    s = service_status + ": " + service_name
                    file1.write(s + "\n")
                    self.slist.append(s)
            serviceDict[service_name] = service_status
         print('\ntext file to dictionary=\n', serviceDict)


    def windows(self):
     file = open(SERCIVE_LIST, 'a')
     file1 = open(STATUS_LOG, 'a')
     file2 = open(DATES, 'a')
     now = datetime.now()
     currTime = now.strftime("%Y/%m/%d %H:%M:%S")
     # date_location = file.tell()
     # sl = currTime + "~" + str(date_location)
     sl = currTime + "~" + str(self.location)
     file2.write(sl + "\n")
     file2.write(sl + "\n")
     # print("\nThe time and date: {} \n".format(currTime))
     file.write(currTime+"\n")
     self.location = self.location + 1
     # file.write("The time and date: {} \n".format(currTime))
     for service in psutil.win_service_iter():
        service_name = service.name()
        # print(service_name)
        service_status = service.status()
        if serviceDict.get(service_name) == None:
            s = "new service:" + service_name
            file1.write(s + "\n")
            self.slist.append(s)

        else:
            sta = serviceDict[service_name]
            if service_status != sta:
                s = service_status + ": " + service_name
                file1.write(s + "\n")
                self.slist.append(s)
        serviceDict[service_name] = service_status
        if service.status() == "running":
            # s = service_name+ "   |   " + service_status
            file.write(service_name + "\n")
            self.location=self.location+1
            # print(service_status)
            service_description = service.description()
            # print(service_description)
            # print("            ")

    def sha1(self,filename):
        BUF_SIZE = 65536  # read stuff in 64kb chunks!
        sha1 = hashlib.sha1()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()
    def start(self,timeUnit):
        status = platform.system()  # print if window or linux
        while not self.stop:
            if (status == "Windows"):
                self.windows()
                commitFile1 = self.sha1(SERCIVE_LIST)
                commitFile2 = self.sha1(STATUS_LOG)
            else:
                self.linux()
                commitFile1 = self.sha1(SERCIVE_LIST)
                commitFile2 = self.sha1(STATUS_LOG)
            time.sleep(timeUnit)
            commitFile3 = self.sha1(SERCIVE_LIST)
            commitFile4 = self.sha1(STATUS_LOG)
            if commitFile1 != commitFile3:
                self.wo.append("The file is different")
                print("The file is different")
            if commitFile2 != commitFile4:
                self.wo.append("The file is different")

    def stopMonitor(self):
        self.stop = True

# if __name__ == '__main__':
