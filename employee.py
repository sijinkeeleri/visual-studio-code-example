
class Employee():
    'Common base class for all employees'
    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
    def displayEmployee(self):
        print ("eid : ", self.eid,", Name : ", self.name,  ", Salary: ", self.salary,  ", did: ", self.did)
    


