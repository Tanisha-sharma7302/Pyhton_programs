N=int(input())
count=0
arr=list(map(int,input().split()))
target=int(input())

for i in range(N):
    for j in range(i+1,N):
        if(arr[i]+arr[j]==target):
            count+=1
print(count)
    

