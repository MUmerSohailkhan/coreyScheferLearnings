import sys

#_____print function_______

'''
print function contain five argument(values,seperator,end,file,flush) values=objects,
seperator=values which seperate the objects,end='what at the end of statement',
file='where to output',flush='to flush the stream'
'''


with open('umer.txt','w') as file:
    print('umer sohail khan',34444,sep='---->',end=' ',file=file,flush=False)
print('sana sohail khan',44444444,sep='---->',end=' ',file=sys.stdout,flush=False)


#Double quotes use
print("my name is umer sohail khan")

#single Quote Use
print('umer')

#Tripple quotes
print('''my name is umer sohail khan
and i am a python developer ,working for undeniable closer mastermind''')

#Variable Use
name='sana sohail khan'
print('my sister name is',name)

#String Concatenation
profession='Pharmacist'
print('my sister name is '+name+' and he is a ',profession)

#percent % sing in print function.it is used in conversion of data
"string value"
print("string value: %s" %name)

"integer"
print("this is integer :%d"%15)

"exponent"
print("this is exponent: %e" %2e10)

"Float"
print("This is float conversion:%f"%5)

"octal"
print("This is octal conversion:%o "%15)

"hexadecimal"
print("this is hexadecimal conversion:%x" %15)

#when using multiple variabel
"use paranathesis when reffering multiple variables"
print("this is hexadecimal conversion:%x %x" %(15,14))

#line break
'\n use use to break the line'
print("my name is umer sohail khan\ni am a python developer")

#print multiple time
print('mughe pyar huaa tha iqrar hua tha '*4)

#\t for tab
print('_'*50,"employee management system",'_'*50,'\n\t1.Add Employee\n\t2.Delete Employee\n\t3.Edit Employee\n\t4.Search Employee\n\t5.Display All Employee')
