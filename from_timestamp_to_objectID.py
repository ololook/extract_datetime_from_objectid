import sys
import time
from bson.objectid import ObjectId
from datetime import datetime
objectid=ObjectId(sys.argv[1])  

timeStamp = time.mktime(objectid.generation_time.timetuple())
timeArray = time.localtime(timeStamp)
createtime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print 
print  "OBJECTID: ",createtime
print
