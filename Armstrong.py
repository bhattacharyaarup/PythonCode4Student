num=int(input("Enter a number"))
copy=num
sum=0
while copy>0:
    r=copy%10
    sum=sum+r**3
    copy=copy//10
if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")
    
