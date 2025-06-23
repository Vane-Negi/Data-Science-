#assignment--2__miniproject____bus fare calculator
print("WELCOME TO OUR BUS")

print("Stops available for the Journey along with their fare:-\n\t1.PS Vivek Vihar-Ram Puri=20\n\t2.ESI Hospital-PS Vivek Vihar=30\n\t3.Surajmal-KarKarDooma=15\n\t4.Mansarovar Park-Shahdara=30")
#then let him select the stop from specifi options
stop=int(input("Select your stop"))
age=int(input('Enter your age'))
#according to the age group  and the stops apply the discount
if stop==1:
    if age<=18:
        
        disc=20-(20*(40/100))
    
        print("FARE FOR YOUR JOURNEY FROM PS Vivek Vihar TO Ram Puri IS:",disc)
    elif age>18 and age<35:
        disc=20-(20*(30/100))
        
        print("FARE FOR YOUR JOURNEY FROM PS Vivek Vihar TO Ram Puri IS:",disc)
    elif age>=35 and age<65:
        disc=20-(20*(10/100))
        
        print("FARE FOR YOUR JOURNEY FROM PS Vivek Vihar TO Ram Puri IS:",disc)
    else:
        disc=20-(20*(50/100))
        
        print("FARE FOR YOUR JOURNEY FROM PS Vivek Vihar TO Ram Puri IS:",disc)
elif stop==2:
    if age<=18:
        disc=30-(30*(40/100))
        print("FARE FOR YOUR JOURNEY FROM ESI Hospital TO PS Vivek Vihar IS:",disc)
    elif age>18 and age<35:
        disc=30-(30*(30/100))
        print("FARE FOR YOUR JOURNEY ESI Hospital TO PS Vivek Vihar IS:",disc)
    elif age>=35 and age<65:
        disc=30-(30*(10/100))
        print("FARE FOR YOUR JOURNEY FROM ESI Hospital TO PS Vivek Vihar IS:",disc)
    else:
        disc=30-(30*(50/100))
        print("FARE FOR YOUR JOURNEY FROM ESI Hospital TO PS Vivek Vihar IS:",disc)
elif stop==3:
    if age<=18:
        
        disc=15-(15*(40/100))
        print("FARE FOR YOUR JOURNEY FROM Surajmal TO KarKarDooma IS:",disc)
    elif age>18 and age<35:
        disc=15-(15*(30/100))
        print("FARE FOR YOUR JOURNEY FROM Surajmal TO KarKarDooma IS:",disc)
    elif age>=35 and age<65:
        disc=15-(15*(10/100))
        print("FARE FOR YOUR JOURNEY FROM Surajmal TO KarKarDooma IS:",disc)
    elif age>=65:
        disc=15-(15*(50/100))
        print("FARE FOR YOUR JOURNEY FROM Surajmal TO KarKarDooma IS:",disc)
elif stop==4:
    if age<=18:
        
        disc=30-(30*(40/100))
        print("FARE FOR YOUR JOURNEY FROM Mansarovar Park TO Shahdara IS:",disc)
    elif age>18 and age<35:
        disc=30-(30*(30/100))
        print("FARE FOR YOUR JOURNEY FROM Mansarovar Park TO Shahdara IS:",disc)
    elif age>=35 and age<65:
        disc=30-(30*(10/100))
        print("FARE FOR YOUR JOURNEY FROM Mansarovar Park TO Shahdara IS:",disc)
    elif age>=65:
        disc=30-(30*(50/100))
        print("FARE FOR YOUR JOURNEY FROM Mansarovar Park TO Shahdara IS:",disc)
else:
    print("ENTER CORRECT STOP")
print("THANKS FOR VISITING THE BUS..('-')")