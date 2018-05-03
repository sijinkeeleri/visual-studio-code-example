from master import Master
class Employee():
    master = Master() 
    def features(self):
        name = input("Name :")
        email = input("Email :")
        salary = input("Salary :")
        print(" master : {}".format(self.master.name))
        
