

#python Variable

"variable nameing rules"
"1.Must begin with letter A-Z or a_z or _"
"2.You cannot use reservered key word as a variable name"
"3.Variable are case senstive"


_name="umer sohail khan"
Name1="Sana Sohail khan"
name2="noor bakht sohail khan"
fruit='apple'
Fruit='mango'
print(Fruit)

#good variable name
'''
1.Choose meaningful name
2.Maintain length of variable name
3.Case for variable name  as(camel,pascal snake)
'''


#assignment
'''
Where the equal sign (=) is used to assign value (right side) 
to a variable name (left side).
'''
studentId='L1F16BSCS093'
stundentName='M Umer Sohail Khan'
salary=500000


#Multiple Assignments
'''
you can assign one value to multiple variable simultanously
'''
# a) 1 to many
umerfather=sanafather=noorfather='Sohail younas khan'
# b) many to many
school,age,number='qazi grammer high school',16,897

print(age)


#swap variable
'''
python swap value in single line
'''
value1='fifty cent'
value2='hundred cent'
print(value1,value2)
value1,value2=value2,value1
print(value1,value2)


#local and global variables
'''
we can create global variable by keyword global
'''
def functionone():
    global stringsd
    stringsd = 'ffff'
    print(stringsd)

def functiontwo():
    print(stringsd)

functionone()
functiontwo()






