N=int(input("Enter a number : "))
sum=0
while(N>0):
    digit=N%10
    sum=sum+digit
    N=N//10
print("Sum of digits of the given number is : " , sum)
