n=int(input("Enter number of rows :  "))
for i in range(1,n+1):
    for j in range(i,n+1):
            print("*" ,end=" ")
    for j in range(2*i-2):
            print(" ",end=" ")
    for j in range(i,n+1):
            print("*",end=" ")
    print()
    # for j in range(i):
    #         print("*" ,end=" ")
    # for j in range(2*n-2*i):
    #         print(" ",end=" ")
    # for j in range(i):
    #         print("*",end=" ")
    # print()
                 
                  
    
            
    
