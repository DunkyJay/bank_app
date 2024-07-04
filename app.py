user_accounts = {}

def main_menu():
  print("Welcome to Mega-Bank, how would you like to proceed?")
  print("1. Open a new account")
  print("2. Login in to an existing account")
  print("3. Exit")
  menu_choice = input()
  if menu_choice == "1":
    account_creation()
  elif menu_choice == "2":
    login()
  elif menu_choice == "3":
    print("Goodbye!")  

def account_creation(): 
  correct_details = False
  while correct_details != True:
    print("Please enter your name")
    name = input()
    print("Please enter your initial deposit")
    initial_deposit = input()
    unique_id = name[0:3].lower() + str(len(user_accounts)+1)
    print("You have entered the following details:")
    print(f"Name: ", name)
    print(f"Initial deposit: £", initial_deposit)
    print(f"Is this correct?")
    print("1. Yes")
    print("2. No")
    confirmation = input()
    if confirmation == "1":
      print("Account created successfully")
      print(f"Your Unique ID is: ", unique_id)
      account_details = [name, initial_deposit]
      user_accounts.update({unique_id : account_details})
      correct_details = True
      main_menu()
    else:
      print("Please try again")

def login():
  correct_details = False
  while correct_details != True:
    print("Please enter your Unique ID or type 'exit' to return to the main menu")
    unique_id = input()
    #print("Please enter your password")
    #password = input()
    if unique_id == "exit":
      correct_details = True
      main_menu()
    
    if unique_id in user_accounts:
      #if user_accounts[unique_id][1] == password:
        print("Login successful")
        correct_details = True
        account_menu(unique_id)
      #else:
        #print("Incorrect password")
    else:
      print("Incorrect Unique ID")

def account_menu(unique_id):
  print("Welcome to your account, please select an option or type 'exit' to return to the main menu")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Account Summary")
  menu_choice = input()
  if menu_choice == "1":
    deposit(unique_id)
  elif menu_choice == "2":
    withdraw(unique_id)
  elif menu_choice == "3":
    account_summary(unique_id)
  elif menu_choice == "exit":
    main_menu()

def deposit(unique_id):
  print("Please enter the amount you would like to deposit")
  deposit_amount = input()
  user_accounts[unique_id][1[1]] = user_accounts[unique_id][1[1]] + deposit_amount
  print("Deposit successful")
  account_menu(unique_id)

def withdraw(unique_id):
  print("Please enter the amount you would like to withdraw")
  withdraw_amount = input()
  if withdraw_amount > user_accounts[unique_id][1[1]]:
    print("Insufficient funds")
    account_menu(unique_id)
  else:
    user_accounts[unique_id][1[1]] = user_accounts[unique_id][1[1]] - withdraw_amount
    print("Withdrawal successful")
    account_menu(unique_id)

def account_summary(unique_id):
  print("Your current balance is: £", user_accounts[unique_id][1[1]])
  print("Recent transactions:")
  print(user_accounts[unique_id][1[2]])
  print("Would you like to return to the account menu?")
  print("1. Yes")
  print("2. No")
  menu_choice = input()
  if menu_choice == "1":
    account_menu(unique_id)
  elif menu_choice == "2":
    main_menu()

main_menu()
