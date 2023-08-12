import pandas as pd

def sign_up():
    print("To create an account, we need a username and password.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    df = pd.read_csv("banking_atm_program/banking.csv", index_col='username')

    if username in df.index:
        print("Username already exists. Please choose a different username.")
        return sign_up()

    savings = 0
    df.loc[username] = [password, savings]
    df.to_csv("banking_atm_program/banking.csv")

    print("Sign up successful")

def login():
    print("To login, we need your username and password.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    df = pd.read_csv("banking_atm_program/banking.csv", index_col='username')

    if username in df.index and df.at[username, ' password'] == password:
        return username, password, df.at[username, ' savings']
    else:
        print("Invalid username or password.")
        return None

def withdraw(savings):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > savings:
        print("Insufficient balance.")
    else:
        savings -= amount
        print(f"Withdrawal of ${amount} successful. Your new balance is: ${savings}")
    return savings

def deposit(savings):
    amount = float(input("Enter the amount to deposit: "))
    savings += amount
    print(f"Deposit of ${amount} successful. Your new balance is: ${savings}")
    return savings

def options(savings):
    while True:
        choice = input("What would you like to do?\nTo withdraw, enter: withdraw.\nTo deposit, enter: deposit.\nTo exit, enter: exit.\nChoice: ")
        if choice == "withdraw":
            savings = withdraw(savings)
        elif choice == "deposit":
            savings = deposit(savings)
        elif choice == "exit":
            return savings

def update_account(username, password, new_savings):
    df = pd.read_csv("banking_atm_program/banking.csv", index_col='username')
    df.at[username, ' savings'] = new_savings
    df.to_csv("banking_atm_program/banking.csv")

while True:
    print("Welcome to Bosch banking.\nPlease login or sign up.")

    loginTRY = input("To create an account, type: sign up.\nTo log in, type: login.\nChoice: ")

    if loginTRY == "sign up":
        sign_up()
    elif loginTRY == "login":
        account_info = login()
        if account_info:
            username, _, savings = account_info
            print(f"Welcome, {username}!")
            print(f"Your current balance is: ${savings}")
            new_savings = options(float(savings))
            update_account(username, _, new_savings)
            print(f"Thank you for using Bosch banking. Your final balance is: ${new_savings}\n\n")
    else:
        print("\nIncorrect input. Please try again.\n")
