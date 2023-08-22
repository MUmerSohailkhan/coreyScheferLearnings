


#list
'''
==>List are used to store multiple items
==>List are created by square brackets
'''

#creation of lists
theList1=['umer',
          'L1F16BSCS0093',
          50000,
          27]
theList2=list(('Narmeen Azhar','L1F16BSCS0092',50000,25))
print('thelist1=',theList1)
print('thelist2=',theList2)

#properties of List
'''
List are ordered
List are changeable
List are mutable objects
List allow duplicates
List contain data of any kind
'''

#accessing the list
'''
by index
'''
print(theList1[2])

'''patch acess'''
print('patch access of list',theList1[0:3])
print('patch access of list',theList1[0:])
print('patch access of list',theList1[:2])
print('patch access of list',theList1[0:-2])
print('patch access of list',theList1[1:2])


'''by loop'''
for x in theList1:
    print(x)

#check on strings
print('umer' in theList1)
print('umer' not in theList1)
if 'Umer' in theList1:
    print('is present')
if 'Umer' not in theList1:
    print('not present')
else:
    print('is present')



#List modification
'''through Index'''
theList1[0]='sana'
print('theList1=',theList1)

'''patch change'''
theList2[0:2]=['Narmeen Azhar Syed','L1f16BSCS0091','University of Central Punjab']
print('theList2=',theList2)

''' insert at index'''
theList1.insert(1,'Azhar saeed')
print(theList1)

'''insert at end'''
theList1.append('Lahore')
print(theList1)

'''remove specific item'''
theList2.remove(50000)
print('theList2 after removing specific item=',theList2)

'''remove specified index'''
theList2.pop(2)
print('theList2 after removing specific index',theList2)
theList1.pop()
print('Applying list.pop()','\ntheList1 after removing specific index',theList1)

'''del the list'''
# del theList1

'''empty the list'''
theList2.clear()
print('Applying list.clear()','\nCleaing all the thelist2',theList2)

#concatenation
theList1.extend(theList2)
print(theList1)
thelist3=theList1+theList2
print('concatenating two list',thelist3)



#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitHaveingAinit = [x for x in fruits if "a" in x]
print(fruitHaveingAinit)


#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print('Applying list.sort()\nList of fruit sorted in ascending order=',thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print('Applying list.sort()\nList of number sorted in ascending order=',thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print('Applying list.sort()\nList of fruit sorted in ascending order=',thislist)

'''customizing sort function'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


'reverse the list'
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copying a list
fruitlist=["banana", "Orange", "Kiwi", "cherry"]
otherfruitlist=list(fruitlist)
print('other fruit list=',otherfruitlist)

thirdfruitlist=otherfruitlist.copy()
print('thirdFruitList=',thirdfruitlist)


# list Methods

'''
list have 11 built-in functions.

append
extend
remove
pop
reverse
sort
copy
insert
index
clear
count
'''


listtotest=["banana", "Orange", "Kiwi", "cherry"]
listtotest[len(listtotest)]='mango'

