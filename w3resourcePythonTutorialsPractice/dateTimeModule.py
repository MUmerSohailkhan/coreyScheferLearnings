import datetime
print(datetime.MINYEAR)
mydate=datetime.date(1996,8,2)
print(mydate)


print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.fromtimestamp(1576800000))

dateToday=datetime.date.today().ctime()
print(type(dateToday))
print(dir(datetime.date))



hijriTime=datetime.timedelta()
