#  Write a program to accept 15 integers from the keyboard in ascending order, assuming that no integer is
#  a zero. Enter a number from keyboard and search in an array using binary search technique. If the
#  number is present display the position of the number, otherwise display Number not found.
#  Python Version 3.5.2

num = []
print ("Enter 10 numbers ")
for i in range(10):
	n=int(input())
	num.append(n)
m=int(input("Enter searched number "))
low=0
high=9
found=0
mid=0
while (low<=high):
	mid=int((low+high)/2)
	if(num[mid] == m):
		found=1;
		break;
	elif(m>num[mid]):
		low=mid+1
	else:
		high=mid-1

if(found==1):
	print ("Numer found")
else:
	print ("Numer not found")
