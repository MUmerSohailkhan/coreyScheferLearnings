import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    host='localhost',
    database='employee'
)
myCursor = mydb.cursor()


class Employee:
    salaryRaisePerYear=0.05
    noOfEmployees=0

    def __init__(self,firstname, lastname, salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
        Employee.noOfEmployees+=1

    def addEmployee(self,firstname, lastname,fathername,CnicNo,salary,designation,address):
        firstname1=firstname
        lastname1=lastname
        fathername1=fathername
        CnicNo1=CnicNo
        salary1=salary
        designation1=designation
        address1=address
        empInfoTupple=(firstname1,lastname1,fathername1,CnicNo1,salary1,designation1,address1)


        employeeInformaitonTableInsertionFormula='Insert into employeeInformation(FirstName,LastName,FatherName,CnicNo,salary,designation,address) Values(%s,%s,%s,%s,%s,%s,%s)'
        myCursor.execute(employeeInformaitonTableInsertionFormula,empInfoTupple)
        mydb.commit()

    def deleteEmployee(self,id):
        employeeDeleteFormula=f'Delete from employeeInformation where empId={id}'
        myCursor.execute(employeeDeleteFormula)
        mydb.commit()

    def editemployeeInformation(self,newInfo,selectedField,empid):


        if selectedField == '1':
            print('first if')
            formu=f"update employeeInformation set FirstName='{newInfo}' where empId={empid}"
            print(formu)
            myCursor.execute(formu)
            mydb.commit()
        elif selectedField == '2':
            myCursor.execute(f"update employeeInformation set lastname= '{newInfo}' where empid={empid}")
            mydb.commit()
        elif selectedField == '3':
            myCursor.execute(f"update employeeInformation set address= '{newInfo}' where empid={empid}")
            mydb.commit()
        elif selectedField == '4':
            myCursor.execute(f"update employeeInformation set fathername= '{newInfo}' where empid={empid}")
            mydb.commit()
        elif selectedField == '5':
            myCursor.execute(f"update employeeInformation set cnicno= '{newInfo}' where empid={empid}")
            mydb.commit()
        elif selectedField == '6':
            myCursor.execute(f"update employeeInformation set salary= '{newInfo}' where empid={empid}")
            mydb.commit()
        elif selectedField == '7':
            myCursor.execute(f"update employeeInformation set designation= '{newInfo}' where empid={empid}")
            mydb.commit()


    def searchEmployee(self, empid):
        myCursor.execute(f'select *from employeeInformation where empId={empid}')
        employeeinformation=myCursor.fetchall()

        tableColumnName=('empid','FirstName','LastName','FatherName','CNIC','Salary','Designation','Address')
        print(tableColumnName)
        for emp in employeeinformation:
            print(emp)

    def displayAllEmployee(self):
        myCursor.execute(f'select *from employeeInformation')
        employeeinformation = myCursor.fetchall()

        tableColumnName = ('empid', 'FirstName', 'LastName', 'FatherName', 'CNIC', 'Salary', 'Designation', 'Address')
        print(tableColumnName)
        for emp in employeeinformation:
            print(emp)


    def salaryRaise(self):
        return self.salary*self.salaryRaisePerYear

    def totalSalary(self):
        return self.salary+self.salaryRaise()

    @classmethod
    def setSalaryRaiasePerYear(cls,amt):
        cls.salaryRaisePerYear=0.09


    @staticmethod
    def isWorkday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

# empl1=Employee('M Umer','Sohail Khan',60000)
# empl2=Employee('Sana','Sohail Khan',1000000)
#
#
# print(empl1.displayFullname())
# print(empl1.salary)
# empl1.salaryRaisePerYear=0.09
# print(empl1.salaryRaise())
# print(empl1.totalSalary())
# import datetime
# my_date=datetime.date(2016,7,10)
# print(Employee.isWorkday(my_date))