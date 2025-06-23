n1=int(input("Enter First number"))
n2=int(input("Enter seconf number"))
op=input("CHOOSE WHAT OPERATION YOU WANT TO PERFORM")
if op=="+":
    print("Result is",n1+n2)
elif op=="-":
    print("Result is",n1-n2)
elif op=="*":
    print("Result is",n1*n2)
elif op=="/":
    print("Result is",n1/n2)
else:
    print("Please enter valid information.")