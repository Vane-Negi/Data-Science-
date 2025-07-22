'''To build a secure, smart banking system where users can register and login using face recognition (via OpenCV), and then perform banking operations like deposit, withdraw, balance check, and transaction history — all stored in MySQL.Modules & Features:
 1. User Management
Register new user with:

Name

Face photo (OpenCV)

Email/Phone

Password

Facial authentication login (OpenCV + Haar Cascade)

Secure user data storage (MySQL)

 2. Banking Operations
Deposit money

Withdraw money

Check balance

Transfer to another account
Transaction history

Admin dashboard to manage users

 3. Security & Verification
Facial recognition as login authentication (OpenCV)

Password-based fallback (if face not detected)

Error handling and logging

 Tech Stack & Requirements
🔹 Python Modules:
opencv-python

mysql-connector-python

numpy

datetime
'''
import mysql.connector
from mysql.connector import Error
import os 
from PIL import Image
from deepface import DeepFace
import cv2
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#database connection

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234567890",
            database="bank"
        )

mycursor = mydb.cursor()
#folder to store registered image
os.makedirs("userfaces",exist_ok=True)

#----user registration----
def capture_photo(filename="captured.jpg"):
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow("Press space to capture photo",frame)
        #press spca to capture 
        if cv2.waitKey(1)&0xFF==ord(' '):  
            print("photo captured Enter you name:")
            name=input().strip()
            if name:
                filename=f"userface{name}.jpg"
                cv2.imwrite(filename,frame)
                print(f"photo save as:{filename}")
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib
                plt.imshow(img)
                plt.title(f"Saved: {name}.jpg")
                plt.axis('off')
                plt.show()
            else:
                print("no name was provided,photo not saved")
            break
    cap.release()
    cv2.destroyAllWindows()
    return filename


def register_user():
    print("\n--- USER REGISTRATION ---")
    print("Capturing user's photo")
    photo_path=capture_photo()
    name=input("Enter you name").strip()
    email=input("Enter your email id").strip()
    phone=(input("Enter your phone number")).strip()
    Pass=input("Enter your password").strip()
   
    try:
        mycursor.execute("INSERT INTO  user (Name,Phone,Email,PASSWORD) VALUES(%s,%s,%s,%s)",(name,phone,email,Pass))
        mydb.commit()
        print("-------------------")

        print("REGISTRATION SUCCESSFUL!!!")
        print("-------------------")

        mycursor.execute("SELECT * FROM user")
        user_records = mycursor.fetchall()
        print("\nCurrent Users:")
        print("ID | Name | Phone | Email")
        print("--------------------------")
        for user in user_records:
            print(f"{user[0]}||{user[1]}||{user[2]}||{user[3]}||")
        
    except Error as err:
        print(f"Database error: {err}")

#face login
def face_login():
    print("\nFace Recognition Login")
    print("LOOK AT THE CAMERA")
    print("---------------------")
    #capture current faace
    cap=cv2.VideoCapture(2)
    ret,current_Face=cap.read()
    cap.release()
#compare with registered face
    mycursor.execute("SELECT photopath FROM user")
    for (photo_path,) in mycursor:
        stored_face=cv2.imread(photo_path)
        if stored_face is not None and np.array_equal(current_Face, stored_face):
            return True
    return False

#password login
def password_login():
    email=input("Enter your email :")
    password=input("Enter your password :")
    mycursor.execute("SELECT * FROM user WHERE email = %s and PASSWORD=%s", (email,password))
    return mycursor.fetchone() is not None

#login
def login():
    if face_login():
        print("Face recognized! Login successful.")
        return True
    else:
        print("Face not recognized. Trying password login...")
    if password_login():
        print("Password accepted! Login successful.")
        return True
    else:
        print("Login failed.")
        return False

#----ATM OPERATIONS---------
class ATM:
    def __init__(self, balance=5000, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transactions = []
    
        
    
    def process(self):
        
        print("\n--- BANKING SERVICES ---")
        print("Insert your card ('card' to continue): ")
        card = input().lower()
        
        if card=="card":
            
            entered_pin = input("Enter your pin(1234): ")
            
            if entered_pin == self.pin:
                while True:
                    print("\n\n1.)Check balance")
                    
                    print("2.)Withdraw money")
                    print("3.)Deposit money")
                    print("4.)Transfer to another account")
                    print("5.) CheckTransaction history")
                    print("6.) Exit")
                    option = int(input("Select your option: "))
                
                    if option == 1:
                        print("Your current balance is:", self.balance)
                    elif option == 2:
                        user_amount = int(input("Enter your amount: "))
                        if user_amount <= self.balance:
                            self.balance -= user_amount
                            print("Your balance is:", self.balance - user_amount)
                            self.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - Withdrew: {user_amount}")
                        else:
                            print("Insufficient funds.")
                    elif option==3:
                        user_amount = int(input("Enter your amount: "))
                        self.balance += user_amount
                        print("AMOUNT SUCCESSFULLY ADDED TO YOUR ACCOUNT!!!!!!")
                        self.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - Deposited: {user_amount}")
                    elif option==4:
                        user_amount = int(input("Enter your amount: "))
                        if user_amount <= self.balance:
                            acc = input("Enter account number to transfer to: ")
                            self.balance -= user_amount  # Actually update balance
                            self.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - Transferred: {user_amount} to account {acc}")
                            print(f"Transfer successful. New balance: {self.balance}")
                        else:
                            print("Insufficient funds.")
                
                    elif option==5:
                        print("\nTransaction History:")
                        print("---------------------")
                        if not self.transactions:
                            print("No transactions recorded.")
                        else:
                            for i ,transaction in enumerate(self.transactions,1):
                                print(f"{i}.{transaction}")
                            print(f"\nCurrent Balance{self.balance}")
                
                    else:
                        print("Invalid option selected.")
                        break

            else:
                print("Wrong pin")
        else:
            print("Invalid card")
            
def main():
    print("\t\t|                   |")
    print("\t\tWELCOME TO OUR BANK")
    print("\t\t-------------------")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            if login():
                atm = ATM()
                atm.process()
        elif choice == '3':
            print("Thank you for using our bank!")
            print("-------------------")

            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    try:
        main()
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()