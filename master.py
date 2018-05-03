from employee import Employee

class Master():
    emp = Employee()

    def features(self):
        name = raw_input("Name :")
        email = input("E-mail :")
        n = input("Number of actions :")
        actions = []
        for i in n:
            i = input("{} :".format(i))
            actions.push(i)
        self.emp.name = input("Employee Name :")
        self.emp.salary = input("Employee Salary :")
        print("Employee Name : {}, Employee Salary : {} ".format(self.emp.name, self.emp.salary))

