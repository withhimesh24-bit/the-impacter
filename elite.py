#how to make pattern in python 

n=int(input("enter the number of rows"))   #take input from user for entering no of rows
i=1       #this initializes the loop
while(i<=n):  #outer loop
    j=1  
    while (j<= i): #inner loop
        print("*",end=" ")
        j+= 1   #this j is increment which moves to the next column position
    print()
    i+=1