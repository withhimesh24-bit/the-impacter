#ATM clone
balance=500000  
username=input("enter your name")  #username
pin=int(input("enter your pin"))   #setup pin
if(username=="Himesh" and pin==1724):
    while True:
        print("Press 1 for Balance")
        print("Press 2 for Deposit")
        print("Press 3 for withdraw")
        
        choice=int(input("enter your choice"))
        if(choice==1):   #for showing your balance
            print("your balance is",balance)
        elif(choice==2):    #to deposit the amount in your ac 
            balance+=int(input("enter the amount"))
            print("your total balance is " ,balance)
        elif(choice==3):   #to withdraw the amount from bank
            amount=int(input("enter your withdrawl amount"))
            if(amount>balance):
                print("insufficient balance")
            else:
                balance-=amount
                print("total balance is",balance)
        else:
            print("invalid option")
    else:
        print("login failed")