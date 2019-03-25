# Python Version 3.5.2

#Define a class Salary described as below:
#Data Member/Instance Variables:
#String name       to store name of the employee
#String phone      to store phone number
#double msalary    to store monthly salary
#double it         to store income tax
#Member methods:
#default constructor to initialize the data members.
#void accept()  to accept name, phone number & monthly salary.
#void compute() to calculate income tax at 15% of annual salary above Rs. 175000
#void display() to display the details of employee
#Write a main method to create object of a class and call the above member methods.

class Salary:
	name=""
	phone=0
	msalary=0.0
	it=0.0
	
	def Salary(self):
		self.name=""
		self.phone=0
		self.msalary=0.0
		self.it=0.0
		
	def accept(self):
		print ("Enter Name of employee, phone number and monthly salary ")
		self.name=input()
		self.phone=int(input())
		self.msalary=float(input())
		
	def compute(self,rate):
		asalary=self.msalary*12.0
		if(asalary>175000):
			self.it=(asalary-175000)*rate/100.0
		else:
			self.it=0.0
			
	def display(self):
		print ("Name = %s Phone Numer = %d Monthly Salary = %.2f Income Tax= %.2f " %(self.name,self.phone,self.msalary,self.it))

		
obj=Salary()
obj.accept()
obj.compute(15)
obj.display()
