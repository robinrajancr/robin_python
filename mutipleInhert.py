class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee():

    def __init__(self,staffnum):
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.staffnumber
class Resident(Person,Employee):
    def __init__(self,first,last,staffnum,address):
        Person.__init__(self,first,last)
        Employee.__init__(self,staffnum)
        self.add=address
    def getaddress(self):
        return self.add
z = Resident("karthik","krishnamurthy","766482","28,bangalore")

print(z.Name())
print(z.GetEmployee())
print(z.getaddress())
