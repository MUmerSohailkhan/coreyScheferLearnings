from Employee import Employee

print("_"*50,"Employee management system","-"*50)
letsContinue='yes'
while letsContinue=='yes':
    print("1.Add Employee\n2.Delete Employee\n3.Edit Employee\n4.Search Employee\n5.Display All Employee")
    list = [1, 2, 3, 4, 5]
    selectedOption = int(input(f"Select by Entering  the option from{list}\n"))
    if selectedOption==1:
        firstname=input("Enter First Name=")
        lastname=input("Enter LastName=")
        fathername=input("Enter fathername=")
        CnicNo=input('CnicNo=')
        salary=input('salary=')
        designation=input('designation=')
        address=input('address=')
        address2="vkjfdvnkjdfnv"
        Employee.addEmployee(address2,firstname,lastname,fathername,CnicNo,salary,designation,address)

    elif selectedOption==2:
        empid=int(input("enter employee id "))
        Employee.deleteEmployee('mvkdfmv',empid)

    elif selectedOption==3:
        print("welcome to Edit the employee")
        empID = input('Enter the Employee EmpId')
        Employee.searchEmployee('eeee', empID)
        print("What To Edit? ,tell by selecting option\n1.Change FirstName\n2.Change LastName\n3.Address\n4.Change FatherName\n5.CNIC\n6.Salary\n7.Designation")
        selectedField=input("Enter your Choice")
        if selectedField=='1':
            newfirstname=input('Enter First Name')
            Employee.editemployeeInformation('nnnn',newfirstname ,selectedField,empID)
        elif selectedField=='2':
            newlastname=input('Enter Last Name')
            Employee.editemployeeInformation('', newlastname,selectedField,empID)
        elif selectedField=='3':
            newAddress=input('Enter New Address')
            Employee.editemployeeInformation('', newAddress,selectedField,empID)
        elif selectedField=='4':
            newFatherName=input('Enter Father Name')
            Employee.editemployeeInformation('', newFatherName,selectedField,empID)
        elif selectedField=='5':
            newCNIC=input('Enter CNIC')
            Employee.editemployeeInformation('', newCNIC,selectedField,empID)
        elif selectedField=='6':
            newSalary=input('Enter Salary')
            Employee.editemployeeInformation('', newSalary,selectedField,empID)
        elif selectedField=='7':
            newDesignation=input('Enter Designation')
            Employee.editemployeeInformation('', newDesignation,selectedField,empID)
        else:
            print("not field other then this")

    elif selectedOption==4:
        empID=input('Enter the Employee EmpId')
        Employee.searchEmployee('eeee',empID)

    elif selectedOption==5:
    # empID=input('Enter the Employee EmpId')
        Employee.displayAllEmployee('')

    else:
        print('no option other then this')

    letsContinue=input('want to continue')




