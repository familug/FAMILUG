#!/usr/bin/env python
import datetime
import time

t = datetime.time(2, 3, 4)
print t

tt = datetime.time()
print tt

now = time.time()
print 'Now timestamp', now
print 'Date convert from ts' , datetime.date.fromtimestamp(now)

today = datetime.date.today()
print 'Today ', today

one_day = datetime.timedelta(days=1)

print 'Comparing date, not full datetime'
yesterday = today - one_day
tomorrow = today + one_day
print 'Yesterday ' , yesterday
print 'Tomorrow ' , tomorrow
print 'Tomorrow - Yesterday ' , tomorrow - yesterday

#Datetime = date + time

d = datetime.datetime.now()
print 'Now : ' , d
for attr in ['year', 'month', 'day', 'hour', 'minute', 'second']:
	print attr, ':', getattr(d, attr)

print 'Today :' , datetime.datetime.today()
print 'UTC now ' , datetime.datetime.utcnow()





