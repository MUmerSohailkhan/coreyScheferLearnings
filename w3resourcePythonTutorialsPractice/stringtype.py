


#strings


'''
definations:
In python string is sequence of character from left to right
string is created with string literals ,enclose in either single ,double quotes
string are arrays of byte represting unicode character
'''

name="Umer Sohail Khan"

#multiline string
'''
you can assing multiline string ,eclosing in triple quote
'''

multiLineString='''m umer
sohail khan,
'''
theString1="cddscsdcsdc"

#accessing the string
'''
by Index
'''
print(name[5])
'''
by loop
'''
for x in name:
    print(x)

'''patch acess'''
print(name[0:])
print(name[:5])
print(name[0:-7])
print(name[-5:-1])


#check on strings
print('Umer' in theString1)
print('umer' not in theString1)
if 'Umer' in theString1:
    print('present')
if 'Umer' not in theString1:
    print('is not present')
else:
    print('Umer is present')


#concatenation
fullsentence='my name is '+ name
print(fullsentence)

#formating
age=27
sentence=f'my name is umer sohial i am {age} year old'


#string modification
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))



#String Methods
# print(dir(sentence))

'''
capitalize
capitalize the first character of string
'''
varToCapatalize='actingordoneinthesameway11212overtimeespeciallsoastobefairraccurate'
print(varToCapatalize.capitalize())

'''
Upper
convert string to upper case
'''
strtoUpperCase=varToCapatalize.upper()
print(strtoUpperCase)

'''
casefold
convert string to lower case
'''
strtocasefold=strtoUpperCase.casefold()
print(strtocasefold)

'''
center
The center() method will center align the string, using a specified character (space is default) as the fill character.
'''
print(name.center(50,'a'))

'''
count
Return a number of time a specified string occour in the string
'''
print(strtocasefold.count('a'))

'''
encode
Returns an encoded version of the string
'''
print(strtocasefold.encode())

'''
endith
Returns true if the string ends with the specified value
'''
print(strtocasefold.endswith('accurate.'))

'''
expandtabs
The expandtabs() method sets the tab size to the specified number of whitespaces.
'''
sentencee='jjjj\tdcdc\tffff'
print(sentencee.expandtabs(10))

'''
find
Searches the string for a specified value and returns the position of where it was found
'''
print(strtocasefold.find('acc'))

'''
formate
The format() method returns the formatted string.
'''
string1='my name is umer sohail khan and i {} year old'
print(string1.format(27))
'-------------------------------to becontinued'

'''
index
Searches the string for a specified value and returns the position of where it was found
'''
print(strtocasefold.index('acc'))


'''
isalnum
Returns True if all characters in the string are alphanumeric
'''
print(strtocasefold.isalnum())

'''
isalpha
Returns True if all characters in the string are alphabetic
'''
print(strtocasefold.isalpha())

'''
isdecimal
Returns True if all characters in the string are alphabetic
'''
decString='123345555'
print(decString.isdecimal())

'''
isdigit
The isdigit() method returns True if all the characters are digits, otherwise False.
'''
decString='123345a555'
print(decString.isdigit())












































#speciale character in string
'''
\ backslash character is used to introduce special character 
there are five special character in python

1. \n
2. \t
3. \\
4. \'
5. \"
'''