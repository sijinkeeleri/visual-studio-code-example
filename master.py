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