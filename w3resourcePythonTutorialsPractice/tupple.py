


# tupple
'''
==>Tupples are used to store multiple items
==>List are created by round brackets
'''

#creations of tupple
thetupple1=('bscs0093',
            'Umer',
            500000,
            26,
            False)
thetupple2=('l1f16bscs0094','Noor Bakht Sohail Khan',500000,22,False)
print('thetupple1 =',thetupple1)
print('thetupple2 =',thetupple2)

#properties of List
'''
Tupple are ordered
Tupple are unchangeable
Tupple are imutable objects
Tupple allow duplicates
Tupple contain data of any kind
'''

#accessing the tupple
'''
by index
'''
print(thetupple1[2])

'''patch acess'''
print('patch access of tupple=',thetupple1[0:3])
print('patch access of tupple',thetupple1[0:])
print('patch access of tupple',thetupple1[:2])
print('patch access of tupple',thetupple1[-3:-1])
print('patch access of tupple',thetupple1[1:2])

'''by loop'''
for x in thetupple1:
    print(x)
for x in range(len(thetupple1)):
    print(thetupple1[x])

#check on strings
print('umer' in thetupple1)
print('umer' not in thetupple1)
if 'Umer' in thetupple1:
    print('is present')
if 'Umer' not in thetupple1:
    print('not present')
else:
    print('is present')


#Tupple modification
'''
Tupple is not modified directly
convert it into list and perform all operations
'''

thetupple1+=thetupple2
print('thetupple1',thetupple1)



# unpacking of tupple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#multiply tupple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tupple methods
'''
count
index
'''



