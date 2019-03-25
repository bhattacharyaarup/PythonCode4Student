#A super class Account contains employee details and a sub class Simple calculates the employees simple interest. 
#The details of the two classes are given below:
#Class Name			Account
#Data Member		
#Name				stores the employee name
#Pan				stores the employee PAN number
#Principal			stores the Principal amount (in decimal)
#acc_no				stores the employee bank account number
#Member Function:
#Account(...)		parameterized constructor to assign value to data member.
#void display()		to display the employee details.

#Class name			Simple
#Data Member
#time				stores the time duration
#rate				stores the rate of interest
#interest			stores the simple interest
#Member function	
#Simple(...)		parameterized constructor to assign value to data members of both the classes.
#void calculate()	calculates the simple interest as (Principal * time * rate)/100
#void display()		displays the employee details along with the rate time and interest.

class Account:
	def __init__(self,n,p,pr,ac):
		self.name=n
		self.pan=p
		self.principal=pr
		self.acc_no=ac
	def display(self):
		print("Name = "+self.name)
		print("PAN = "+self.pan)
		print("Principal = %d" %self.principal)
		print("A/c Number = %d" %self.acc_no)

class Simple(Account):
	def __init__(self,n,p,pr,ac,t,r):
		Account.__init__(self,n,p,pr,ac)
		self.time=t
		self.rate=r
		self.interest=0.0
	def calculate(self):
		self.interest=(self.principal*self.rate*self.time)/100.0
	def display(self):
		Account.display(self)
		print("Time = %d" %self.time)
		print("Rate = %0.2f" %self.rate)
		print("Interest %0.2f" %self.interest)
		
		
		
obj=Simple("Amit","AHQPB5487A",10000,101,5,7.5)
obj.calculate()
obj.display()