


#introduction
'''
Variables can store data of different types, and different types can do different things.
1.Type represent the kind of value and determine how the value can be used
2.Everything in python is object
3.Evey object have identity, type and value
4.To determine the type python provide type function type()
'''


'''
Datatypes
Python contain following built in broad datatype, it further divide into sub-types
1.Numbers Type
    1.1)int     1.2)float      1.3)complex
2.Text Type
    2.2)String
3.Mapping Type
    3.1)Dictionary
4.Sequence Type
    4.1)Tupple  4.2)Range      4.3)List
5.Set Type
    5.1)Set     5.2)Frozen Set
6.Boolean Type
    6.1)Bool
7.Binary Type
    7.1)Bytes   7.2)ByteArray  7.3)Memory View
8.None Type
    8.1)None     
'''

#Getting the Data type by type() function
fullName='M Umer Sohail khan'
print(type(fullName))



#setting the Data Type
'string'
FullName="Sana sohail Khan"
'int'
salary=50000
'float'
height=5.4
'complex'
value1=5+4j
'Dictionary'
biodate={
    'name':'umer sohail khan',
    'age':27,
    'salary':500000,
    'height':5.4
}
'Tupple'
tupple1=('sami ullah khan',)
'range'
x=range(10,30)
'list'
listofelectronics=['bulb','tubelight','fan','energy saver']
'set'
set1={1,2,3,4,5,'vggg',5,5,5,5}
print(set1)
'frozen set'
froznset1=frozenset({2,3,4,5,6,7,7})
print(froznset1)
'boolean'
z=True
'byte'
x = b"Hello"
'bytearray'
x = bytearray(5)
'memory view'
x = memoryview(bytes(5))
'None type'
x = None












