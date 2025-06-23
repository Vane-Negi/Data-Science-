uni=int(input("Enter the Unit of electricity :- "))
rate=5
if uni<=200:
    print("ELECETRICTY BILL=0")
else:
    print("ELECTRICITY BILL =",(uni-200)*rate)