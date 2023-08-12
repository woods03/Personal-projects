# Little programing where we simulate the working of bank account/multiple bank accounts
import csv
#sign up function
def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password")
    savings = 0 #new account always 0 saving
    with open("banking.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, savings])
    print("Sign up succesfull")
    





while True:
    print("Welcome at Bosch banking. \nPlease login and select what u want to do!")

    # Here we will work with our csv file to store passwords and usernames so a user can login, besides that we will store the bank savings.
    inp = False
    print("For making a account type: sign up.\nFor logging in type: Login.")
    while (inp == False):
        loginTRY = input(":")
        if loginTRY == "sign up":
            
        elif loginTRY == "login":
            
        else:
            print("Input is incorrect please try again.\nFor making a account type: sign up.\nFor logging in type: Login.")