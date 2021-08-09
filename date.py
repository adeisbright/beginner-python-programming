from datetime import date , time , datetime  , timedelta 
import time 

now = datetime.now() #time()
print(now.year ) 
print(now.strftime("%H:%M:%S") ) #Formats date into readable string a weekday short version , d , b month short version , w as number , H , y , m , s , z
form_date = datetime(2020 , 4 , 2) 
print(form_date.strftime("%D")) 

import time 
t = time.localtime()
current_time = time.strftime("%H:%M:%S" , t)
print(current_time)
# CONVERT from_date to timestamp 
timenumber = datetime.timestamp(form_date) 
print(timenumber) 
assumed_time = 12334455666 
event = datetime.fromtimestamp(assumed_time) 
print(event)
seconds1970 = time.time() # returns the second elapsed since 1970 time.localtime(n) will return a struct time.gmtime(sec)
local_time = time.ctime(8900000000) # returns local time using seconds provided 
print(seconds1970 , local_time)  
print("I am going to sleep for 20s")
time.sleep(20) 
print("Now I am awake") 
maketime = time.mktime(900099)
asctime  = time.astime(2019 , 12 , 3 , 44 , 4 , 4) 
print(maketime , asctime) 