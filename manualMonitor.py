
from datetime import datetime
from monitor import monitor

SERCIVE_LIST = "serviceList.log"
DATES = "date.txt"



class manualMonitor:
    #init the manualMonitor obj by monitor object
    def __init__(self):
        pass
        # self.mon=monitor

    #
    def start(self,strtDate,endDate):
     try:
      file1 = open(SERCIVE_LIST, 'r')
     except:
         return
     serviceDict1 = {}
     serviceDict2 = {}
     lines1 = file1.readlines()
     #reading the help file that helps us to save the dates in the "serviceList.log" file
     file2=open(DATES,'r')
     lines2 = file2.readlines()

     #getting the times from the user as inputs
     times=[]
     times.append("0")
     i=1
     dateObj=[]
     #appending all the dates into a list
     for line in lines2:
        times.append(line.split('~'))
        datetime1=times[2*1-1][0]
        dateObj.append(datetime.strptime(datetime1, "%Y/%m/%d %H:%M:%S"))
        i+=1
     #convert the input dates to our format
     strtDate=datetime.strptime(strtDate, "%m/%d/%Y %H:%M:%S")
     endDate=datetime.strptime(endDate, "%m/%d/%Y %H:%M:%S")

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
     posA = int(times[strtTime][1])+1
     posB = int(times[strtTime2][1])
     while posA < posB:
            if not lines[posA].startswith("2022/"):

                serviceDict1[lines[posA]] = "is running"
                posA=posA+1
     #doing the same with the second time
     posA = int(times[endTime][1])+1
     if endTime2 <len(times):
         endTime2=int(times[endTime2][1])-1
     else:
         endTime2=endTime2+1
     while posA < (endTime2):
            if not lines[posA].startswith("2022/"):
                serviceDict2[lines[posA]] = "is running"
                posA=posA+1
     print(posA , len(times))
     if posA == len(lines)-1:
            serviceDict2[lines[posA]] = "is running"
            print("dd")

     #print the changes between the first time and second time
     str=""
     # print(serviceDict2)
     # print(serviceDict1)

     for key in serviceDict1:
        if serviceDict2.get(key) == None:
            str += "The service {} stopped".format(key[0:(len(key)-1)])
            str += '\n'
     for key in serviceDict2:
        if serviceDict1.get(key)==None:
            str += "The service {} begin".format(key[0:(len(key)-1)])
            str += '\n'
     print(str)
     return str

if __name__ == '__main__':
    s1="2022/03/27 19:55:54"
    s2="2022/03/27 19:57:00"
    m= monitor
    mm=manualMonitor(m)
    mm.start(s1,s2)
    # manualMonitor()

# 22-03-25 12:35:56
# 2022-03-25 12:35:59
