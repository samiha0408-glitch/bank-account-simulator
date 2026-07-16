from bank_account import BankAccount
my_account = None

def start_menu():
   print("==== BANK ACCOUNT =====")
   print("1. Create Account")
   print("2. Exit")

def bank_menu():

   print("==== BANK ACCOUNT =====")
   print("1. Account Summary")
   print("2. Deposit Money")
   print("3. Withdraw Money")
   print("4. Exit")

def pause():
   input("Press Enter to return to the menu...")

while True:
   start_menu()
   user =int(input("Enter your choice: "))
   if user == 1:
      account_holder = input("Enter your name: ").title()
      account_number = int(input("Enter your account number: "))
      balance = float(input("Initial deposit ammount: "))

      my_account = BankAccount(
         account_holder,
           account_number,
             balance)
      break
   else: 
      print("Thank you for visiting us!")
      break

if my_account is not None:
   while True:
      bank_menu()
      choice = int(input("Enter your choice: "))
      if choice == 1:
         print(f"Your balance is: ${my_account.balance}")
         print(f"Transations: {my_account.transaction_count}")
         pause()

      elif choice == 2:
         while True:
            print (f" Your current balance:$ {my_account.balance}")
            amount = float(input("Enter the amount you want to deposit: "))
            my_account.deposit(amount)
            if my_account.deposit(amount):
               print(f"New Balance: ${my_account.balance}")
            else:
               print("Enter a positive amount!")

            amount1= input("Want to deposit more?[y/n]:")
            if amount1 == "y" :
               continue
            else:
               break
         pause()

      elif choice == 3:
         while True:
            print (f" Your current balance:$ {my_account.balance}")
            amount2 = float(input("Enter the amount you want to withdraw: "))
            if my_account.withdraw(amount2):
               print(f"New Balance: {my_account.balance}")
            else:
               print("Enter a valid amount!")
            
            amount3= input("Want to withdraw more?[y/n]:")
            if amount3 == "y" :
               continue
            else:
               break
         pause()
               
      elif choice == 4:
         print("Thank you for visiting our bank🤎")
         break
      else:
         print("Invalid option. Please choose 1,2,3 or 4!") 


      



