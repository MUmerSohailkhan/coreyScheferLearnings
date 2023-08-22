


#Dictionary
'''
==>Dicitionary are used to store multiple items with key value pair
==>List are created by Curly bracket {}
'''

#creation of Dictionary

theDict1={'Name':'Umer',
          'Rno':'0093',
          'age':27,
          }
print('TheDict1',theDict1)
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#properties of Dictionary
'''
Dictionary are ordered
Dictionary are changeable
Dictionary are mutable
Dictionary not allow duplicates
Dictionary are contain data of any kind
'''

#accessing the dictionary
'''access by key name'''
print('Accessing the value in the dictionary by key name',theDict1['Name'])

'by get method'
x = theDict1.get("Name")
print(x)

'get keys'
k=theDict1.keys()
print(k)

'get values'
v=theDict1.values()
print(v)

'get  item wil return every item as tuples in a list'
# i=theDict1.items()
# print(i)
# for x in i:
#     print(x[1])

'''by loop'''
for x in theDict1.items():
    print(x)

# for y in theDict1.

#check on Dictionary
if 'Name' in theDict1:
    print('yes')
else:
    print('no')

# dictionary modifications
'by refering key'
theDict1['Name']='sana sohail khan'
print(theDict1)
theDict1['address']='gwawamore'


'by update method'
theDict1.update({'fathername':'sohail younas khan'})
print(theDict1)

'by pop method'
theDict1.pop('address')
print(theDict1)

'by del'
del theDict1['salary']
print(theDict1)

'clear all the dictionary'
theDict1.clear()
print(theDict1)


# copy a dictionary
mydict=thisdict.copy()
print(mydict)