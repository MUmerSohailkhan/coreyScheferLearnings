print("My name is",'Umer','My age is',27,sep=' ',end='',flush=False)
print('I am software Engineer')
with open('data.txt','w') as file:
    print("My name is", 'Umer', 'My age is', 27, sep=' ', end='',file=file, flush=False)
print('''my name is umer
sohail khan and i am software engineer''')

fullName='M Umer Sohail Khan'
print('FullName : %s'%fullName)
print('Age : %d'%27)
print('Salary : %e%s'%(2e10,'$'))
print('Height : %f%s'%(5.4,'ft'))
print('octal : %o'%15)
print('Hexadecimal : %x'%15)
print('~__ ~'*5)

# Variable Practice
myRegistrationNo='L1F16BSCS0093'
sanaFather=umerFather=noorFather='Sohail Younas Khan'
startDate,endDate,Major=2016,2021,'BSCS'
print(sanaFather,umerFather,noorFather,startDate,endDate,Major)
endDate,startDate=startDate,endDate
print(startDate,endDate)
global university
university='univerdity of central punjab'
print(university)

#Data types Practice
value=None
print(type(value))
age=27
x=range(10,30)
print(x)

#String Practice
newString="A set is a collection of items where each item is unique. This is derived from the mathematical concept of the same name."
print(newString[0:20])
# for x in newString:
#     print(x)
if 'items' in newString:
    print('yes')
else:
    print('No')

#boolean practice
x=bool(1)
if x is True:
    print('yes')
else:
    print('no')

#operators Practice


#List
theList1=['M Umer Sohail Khan','L1F16BSCS0093',27,'BSCS']
print(theList1[0])
print(theList1[0:2])
for x in theList1:
    print(x)

if 27 in theList1:
    print('yes')
else:
    print('No')

theList1[2]=26.5
print(theList1)

#Dictionary
theDictionary1={
    'name':'M Umer Sohail Khan',
    'age':27,
    'registration no':'L1F16BSCS0093',
    'Course':'BSCS'
}
