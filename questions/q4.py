N=int(input())
count=0
for i in range(N):
    data=input().split()
    marks=int(data[0])
    atten_per=int(data[0])
    if(marks>=75 and atten_per>=80):
        count+=1
print(count)


    

