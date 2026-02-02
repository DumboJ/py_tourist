import time
from datetime import datetime, timedelta

#时间戳
time.time()
#time.struct_time(tm_year=2026, tm_mon=1, tm_mday=31, tm_hour=21, tm_min=51, tm_sec=16, tm_wday=5, tm_yday=31, tm_isdst=0)
#标准化输出 日期时间 2026-01-31 21:49:35
time.strftime('%Y-%m-%d %X',time.localtime())
#字符日期转回 local_time
time.strptime('2026-01-31 21:49:35',"%Y-%m-%d %H:%M:%S")


#当前日期
datetime.today()    #datetime.datetime(2026, 1, 31, 22, 12, 42, 552027)
datetime.now()      #datetime.datetime(2026, 1, 31, 22, 13, 22, 333509)

#时间偏移
print(datetime.today()-timedelta(days=-1)) #2026-02-01 22:16:25.567279

sum_r = 0
for i in range(1,11):
    sum_r += i
print(sum_r)

while(sum_r<100):
    sum_r+=7
print(sum_r)