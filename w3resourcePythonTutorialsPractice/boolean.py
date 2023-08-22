

#boolean
'''
Boolean represent one of two values    (TRUE/FALSE)

'''



#Evaluate Every Value using bool function
'string'
print(bool('something'))
'empty string'
print(bool(''))
'number'
print('Number with zero value=',bool(0))
'number'
print('Number with non-zero value=',bool(1))
'empty list'
print(bool([]))
'non-empty list'
print(bool(['a','b','c']))


lst=['umer','khan']
if bool(lst)==False:
    print('list is empty')
else:
    print('list containe something')



#everything evaluated

'''
False
    (),[],{},"",0,False
    
True
    everything true except above
'''

