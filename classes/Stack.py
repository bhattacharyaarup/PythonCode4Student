#Class Name			Stack
#Data members/Instance variables
#arr[]				Integer array to hold numbers
#max				Integer to hold maximum capacity of stack array.
#tos				Integer to point to the top of the stack.
#Member Function
#Stack(int m)		Constructor to initialize max=m and tos to -1
#void push(int)		Adds a number to the top of the stack. If possible, otherwise displays a message Stack full. 
#					Start removing data.
#void pop()			Removes the number from the top, if possible otherwise display Stack empty

class Stack:
	def __init__(self,m):
		self.arr=[]
		self.max=m
		self.tos=-1
		
	def push(self,num):
		if(self.tos==self.max-1):
			print("Stack is full")
			return
		else:
			self.arr.append(num)
			self.tos=self.tos+1
	def pop(self):
		if(self.tos==-1):
			print("Stack is empty")
			return
		else:
			print("%d is popped from stack" %(self.arr[self.tos]))
			self.tos=self.tos-1
			self.arr.pop()
	
	
obj=Stack(5)
ch=0
while(ch!=3):
	print("1. Push")
	print("2. Pop")
	print("3. Exit")
	ch=int(input())
	if(ch==1):
		num=int(input("Enter a number "))
		obj.push(num)
	elif(ch==2):
		obj.pop()
		