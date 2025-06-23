print("------CREATE ACCOUNT-------")
set_user=input("Enter  username")
set_pass=int(input("Enter your password"))
print("\t\t\t\t NOW LETS LOGIN IN YOUR ACCOUNT")
for i in range(0,3):
    user=input("Enter you correct username:")
    passw=int(input("Enter your password"))
    if set_user==user and set_pass==passw:
        print(user,"WELCOME IN OUR SYSTEM")
        break;
    else:
        print("OOPS.....ENTER CORRECT CREDIANTILS")
        continue
    print("YOUR RIES")