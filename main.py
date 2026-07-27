#  Project--02 || Bank Management System
#  using Python

import json


def save_accounts():
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, indent=4)

def load_accounts():
    try:
        with open('accounts.json', 'r') as f:
           return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

accounts = load_accounts()


while True:
    print('\n===== Bank Management System =====\n')
    print('1. Create Account')
    print('2. View All Accounts')
    print('3. Search Account')
    print('4. Deposit Money')
    print('5. Withdraw Money')
    print('6. Transfer Money')
    print('7. Check Balance')
    print('8. Delete Account')
    print('9. Total Accounts')
    print('10. Exit')

    choice = input('Enter your choice: ')



    # 1. CREATE-ACCOUNT :
    if choice == '1':
        account_id = int(input('Enter account ID: '))
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        phone_no = input('Enter your phone number: ')
        balance = float(input('Enter your initial balance: '))


        account = {
                  'id': account_id,
                  'name': name,
                  'age': age,
                  'phone_no': phone_no,
                  'balance': balance
        }


        found = False

        for existing_account in accounts:
            if existing_account['id'] == account_id:
                  found = True
                  print(f'Account ID {account_id} already exists')
                  break

        if not found:
            accounts.append(account)
            save_accounts()
            print('Account created successfully')




    # 2. VIEW-ALL-ACCOUNTS :
    elif choice == '2':
        if not accounts:
            print('No accounts found')
            continue

        else:
            print('\nAccounts List:\n')
            for account in accounts:
                print("------------------------------------")
                print(f"Account ID   :{account ["id"]}")
                print(f"Name         :{account["name"]}")
                print(f"Age          :{account["age"]}")
                print(f"Phone Number :{account["phone_no"]}")
                print(f"Balance      :{account["balance"]:.2f}")
                print("------------------------------------")




    # 3. SEARCH-ACCOUNTS :
    elif choice == '3':

        if not accounts:
            print('No accounts found')
            continue

        search_id = int(input('Enter account ID search: '))

        found = False

        for account in accounts:
            if account['id'] == search_id:
                print('\nAccount Found')
                print('Account ID:'    , account['id'])
                print('Name:'          , account['name'])
                print('Age:'           , account['age'])
                print('Phone Number:'  , account['phone_no'])
                print('Balance:'       , account['balance'])
                found = True
                break

        if not found:
            print('\nAccount not found')




    # 4.  DEPOSIT-MONEY :
    elif choice == '4':

        if not accounts:
            print('No accounts found')
            continue

        deposit_id = int(input("Enter Account ID: "))

        found = False

        for account in accounts:
            if account["id"] == deposit_id:
                found = True

                deposit_amount = float(input("Enter deposit amount: "))

                if deposit_amount <= 0:
                   print('\nInvalid deposit amount')
                else:
                   account["balance"] += deposit_amount
                   print("\nDeposit successful!")
                   print(f"New Balance: ₹{account['balance']:.2f}")
                   save_accounts()
                   break

        if not found:
            print("Account not found")


    # 5. WITHDRAW-MONEY :
    elif choice == '5':
        withdraw_id = int(input('Enter Account ID: '))

        found = False

        for account in accounts:
            if account["id"] == withdraw_id:
                found = True

                withdraw_amount = float(input("Enter withdrawal amount: "))

                if withdraw_amount <= 0:
                    print('\nInvalid withdrawal amount')

                elif withdraw_amount > account["balance"]:
                    print("\nInsufficient balance!")
                    print(f"Current Balance: ₹{account['balance']:.2f}")

                else:
                    account["balance"] -= withdraw_amount
                    print("\nWithdrawal successful!")
                    print(f"New Balance: ₹{account['balance']:.2f}")
                    save_accounts()
                    break

        if not found:
            print("Account not found")



    # 6. TRANSFER_MONEY :
    elif choice == '6':

        try:
            sender_id = int(input("Enter Sender Account ID: "))
            receiver_id = int(input("Enter Receiver Account ID: "))

        except ValueError:
            print("\nError: Please enter valid numeric Account IDs.")
            continue


        if sender_id == receiver_id:
            print("\nError: Sender and Receiver cannot be the same account.")
            continue
        sender_account = None
        receiver_account = None

        for account in accounts:

            if account["id"] == sender_id:
                sender_account = account

            if account["id"] == receiver_id:
                receiver_account = account

            if sender_account is not None and receiver_account is not None:
                break

        if sender_account is None or receiver_account is None:
            print("\nError: sender or receiver account not found.")
            continue


        try:
            transfer_amount = float(input("Enter Transfer Amount: ₹"))

        except ValueError:
            print("\nError: Please enter a valid amount.")
            continue


        if transfer_amount <= 0:
            print("\nError: Transfer amount must be greater than 0.")

        elif transfer_amount > sender_account['balance']:
            print("\nInsufficient balance!")
            print(f"Current Balance: ₹{sender_account['balance']:.2f}")

        else:

            sender_account['balance'] -= transfer_amount
            receiver_account['balance'] += transfer_amount

            save_accounts()

            print("\n========== Transfer Successful ==========")
            print(f"Transferred Amount : ₹{transfer_amount:.2f}")
            print(f"From Account    : {sender_id}")
            print(f"To Account      : {receiver_id}")
            print(f"Sender Balance  : ₹{sender_account['balance']:.2f}")
            print(f"Receiver Balance: ₹{receiver_account['balance']:.2f}")


    # 8. DELETE ACCOUNT:
    elif choice == "8":

        if not accounts:
            print('No accounts found')
            continue

        try:
            delete_account_id = int(input("Enter Account ID to delete: "))
        except ValueError:
            print('Account ID must be an integer')
            continue

        found = False

        for account in accounts:
            if account["id"] == delete_account_id:
                accounts.remove(account)
                print(f'Account {account["id"]} deleted successfully!')
                save_accounts()
                found = True
                break

        if not found:
            print("Account not found.")

    # 9. TOTAL BOOKS:
    elif choice == "9":

        if not accounts:
            print('No accounts found')
            continue

        total_money_in_bank = 0

        for account in accounts:
            total_money_in_bank += account['balance']

        print("\n========== Bank Statistics ==========\n")
        print("Total Money in Bank: ", total_money_in_bank)
        print("Total Accounts: ", len(accounts))
        print("\n========================================\n")


    # 10. EXIT
    elif choice == "10":
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice.")
        print("Please enter a number between 1 and 10.")



