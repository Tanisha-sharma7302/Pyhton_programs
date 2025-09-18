N=int(input())
arr=list(map(int,input().split()))
Pass=0
Fail=0

for i in arr:
    if(i>35):
        Pass+=1
    else:
        Fail+=1
print(Pass)
print(Fail)



    

        


