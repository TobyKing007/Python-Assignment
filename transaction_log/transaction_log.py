

def deposit(amount, account_balance, transactions):
    account_balance += amount
    transactions.append (f"Deposited: ₦{amount} | New Balance: ₦{account_balance}")
    print(transactions[-1])
    return account_balance


def withdrawal (amount, account_balance, transactions):
    if amount <= account_balance:
        account_balance -= amount
        transactions.append(f"Withdrew: ₦{amount} | New Balance: ₦{account_balance}")
        print(transactions[-1])

    else:
        transactions.append("Insufficient funds")
        print("Insufficient funds")
    return account_balance


def all_transactions(transactions):
    if transactions == []:
        print("No transactions yet")

    else:
        print ("Transactions history")
        index = 1
        for activities in transactions:
            print(f"{index}. {activities}")
            index+=1


def main():
    account_balance = 0
    transactions = []
    
    print(" WELCOME TO TRANSACTION LOG APP")

    while True:
        print("\n1. Deposit")
        print("2. Withdrawal")
        print("3. Show all transactions")
        print("4. Exit")        
      
        menu_choice = input("Enter your choice: ")

        if menu_choice == "1":
            amount = int(input("Enter deposit amount: "))
            account_balance = deposit(amount, account_balance, transactions)

        elif menu_choice == "2":
            amount = int(input("Enter withdrawal amount: "))
            account_balance = withdrawal(amount, account_balance, transactions)

        elif menu_choice == "3":
            all_transactions(transactions)

        elif menu_choice == "4":
            print(f"\nAccount balance is: ₦{account_balance} " )
            print (f"\nTransaction history" )
            all_transactions(transactions)
            print("\nThank you for using Transaction Log App!")
            break

        else:
            print("\n INVALID INPUT. PLEASE ENTER 1-4")

main()
