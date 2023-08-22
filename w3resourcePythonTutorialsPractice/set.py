

# Sets
'''
==>Sets are used to store multiple items
==>Sets are created by curly braces
'''

#creations of tupple
theSet1={
    "apple",
    "banana",
    "cherry"
}
theSet2={'kiwi','watermelon','carrot'}
print(theSet1)


#properties of Set
'''
Set are unordered
Set are unchangeable
set are mutable
Set not allow duplicates
Set contain data of any kind
'''

#accessing the set
'''by loop'''
for x in theSet1:
    print(x)

#check on strings
print('apple' in theSet1)
print('umer' not in theSet1)
if 'Umer' in theSet1:
    print('is present')
if 'Umer' not in theSet1:
    print('Umer is not present in this name')
else:
    print('Umer is present')

# modification
'remove item'
theSet1.remove('apple')
print('After Removing item from set',theSet1)

'discard item'
theSet1.discard('apple')
print('After discarding item from set',theSet1)

'pop item'
theSet2.pop()
print('after poping the set',theSet2)

'clear set'
theSet2.clear()
print('after clearing the set',theSet2)

# concatenation
theSet1.add('guave')
print('theset1 after adding guave =',theSet1)
'''add any iterable'''
li=['cabbage','reddish']
theSet1.update(li)
print('after adding li in the theset1=',theSet1)


# methods

'keep only duplicates'
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print('Applying intersection update',x)


'keep only duplcate and return new set'
z = x.intersection(y)
print(z)

'keep all but not duplcate'
x.symmetric_difference_update(y)
print(x)

'keep all but not duplcate return new set'
z = x.symmetric_difference(y)
print(z)

'difference'
z = x.difference(y)
print(z)


'difference update'
'Remove the items that exist in both sets'
x.difference_update(y)
print('difference update',x)






