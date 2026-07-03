def menu():
   print("==== BANK ACCOUNT =====")
   print("1. Check Balance")
   print("2. Deposit Money")
   print("3. Withdraw Money")
   print("4. Exit")

def pause():
   input("Press Enter to return to the menu...")

balance = 1000
transaction_count = 0
while True:
   menu()
   choice = int(input("Enter your choice: "))
   if choice == 1:
      print(f" Your balance is: ${balance}")
      print(f" Transactions: {transaction_count}")
      pause()

   elif choice == 2:
      while True:
         print (f" Your current balance:$ {balance}")
         amount = float(input("Enter the amount you want to deposit: "))
         if amount > 0:
            balance += amount
            transaction_count += 1
            print(f'Your new balance is : {balance}')
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
         print (f" Your current balance:$ {balance}")
         amount2 = float(input("Enter the amount you want to withdraw: "))
         if balance < amount2 :
            print("Insufficient Balance!!")
         else:
            balance -= amount2
            transaction_count += 1
            print(f'Your new balance is : {balance}')
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


   



