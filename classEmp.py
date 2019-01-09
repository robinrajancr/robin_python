class employee:
 def __init__(self, Emp_name, Emp_age, Emp_sal):
  self.Emp_name = Emp_name
  self.Emp_age = Emp_age
  self.Emp_sal = Emp_sal
 def display(self):
     print ("Employee details " + self.Emp_name,self.Emp_age,self.Emp_sal)
p1 = employee("Robin","37","10000")
p1.display()

