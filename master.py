from employee import Employee

class Master():
    def addemployee():
        n = input("number of employees :")
        
        for i in range(0, n):
            eid = input(" employee id : ")
            name = raw_input("Name : ")
            salary = input(" Salary : ")
            did = input("did : ")
            emp = Employee(eid, name, salary, did)
            emp.displayEmployee()

    addemployee()
    def permission():
        input("Enter 5 master permission : ")
        for i in range(1,6):
            permission = input("{} :".format(i))
        b = input("Save Changes (Y/N) :")
        if b == 'Y' or b == 'y':
            print("save successfully")

        else:
            print("unsaved permissions")
        
