x=lambda x:x+10
print(x(4))

theString1='umer'
theString2='Sohial khan'
theString3='i am programmer python developer and content creator'

x=lambda a,b,c:a+b+c
print(x(theString1,theString2,theString3))



def myfun(n):
    return lambda a:a*n

doubler=myfun(2)
tripler=myfun(3)

print('Doubler',doubler(10))
print('Tripler',tripler(3))
