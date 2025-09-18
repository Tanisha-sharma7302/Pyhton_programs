N=int(input())
arr=list(map(int,input().split()))
max=min=arr[0]
for i in arr:
    if(i>max):
        max=i
    if(i<min):
        ans=i
print(max,min)







        