

import time,os
from datetime import datetime
from VarConfig import screenPicturesDir
import time,re


#获取当前的日期
def getCurrentDate():
    timeTup=time.localtime()
    currentDate=str(timeTup.tm_year)+"-"+str(timeTup.tm_mon)+"-"+str(timeTup.tm_mday)
    return currentDate


#获取当前的时间
def getCurrentTime():
    timeStr=datetime.now()
    nowTime=timeStr.strftime('%H-%M-%S')
    return nowTime



def today():
    import datetime
    date=datetime.date.fromtimestamp(time.time())
    res=re.findall('[0-9]{2,4}',str(date))
    today=res[1]+res[2]
    year=res[0]
    for i in today[0]:
        if int(i)==0:
            today=today[1::]
            today=year[2::]+today
        else:
            today = year[2::] + today
    return today



#获取截图存放的目录
def createCurrentDataDir():
    dirName=os.path.join(screenPicturesDir,getCurrentDate())
    if not os.path.exists(dirName):#不存在在个文件夹？
        os.makedirs(dirName)
    return dirName


