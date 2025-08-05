n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
while True:
    choice=input("Operation Choice(1.Add,2.Subtract,3.Multiple,4.Division):")
    if choice=="1":
        print("Result:",n1+n2)
        break
    elif choice =="2":
        print("Result:",n1-n2)
        break
    elif choice=="3":
       print("Result:",n1*n2)
       break
    elif choice=="4":
        print("Result:",n1/n2)
        break
    else:
        print("Invalid Choice")
        break
