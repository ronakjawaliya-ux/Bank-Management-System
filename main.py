import json


def save_accounts():
    try:
        with open('accounts.json','w') as f:
            json.dump(accounts,f,indent=4)

    except Exception as e:
        print("Error saving data:", e)


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
    print('4. Update Account')
    print('5. Deposit Money')
    print('6. Withdraw Money')
    print('7. Transfer Money')
    print('8. Check Balance')
    print('9. Delete Account')
    print('10. Total Accounts')
    print('11. Exit')

    choice = input('Enter your choice: ')



    # 1. CREATE ACCOUNT
    if choice == '1':

        # Validate ID
        try:
            account_id = int(input('Enter account ID: '))
        except ValueError:
            print('\nError: Please enter valid numeric Account IDs.')
            continue

        if account_id <= 0:
            print("Account ID must be positive")
            continue

        # Validate Name
        name = input('Enter your name: ').strip()
        if not name:
            print('Name cannot be empty')
            continue

        # Validate Age
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Age must be an integer.")
            continue

        # Prevent zero or negative age
        if age <= 0:
            print("Age must be greater than zero.")
            continue

        if age > 120:
            print("Age must be 120 or less.")
            continue

        # Validate Phone number
        phone_no = input("Enter your phone number: ").strip()

        if not phone_no:
            print("Phone number cannot be empty.")
            continue

        if not phone_no.isdigit():
            print("Phone number must contain digits only.")
            continue

        if len(phone_no) != 10:
            print("Phone number must contain exactly 10 digits.")
            continue

        # Validate Balance
        try:
            balance = float(input('Enter your initial balance: '))
        except ValueError:
            print('\nError: Please enter valid numeric balance.')
            continue

        # Prevent negative age
        if balance < 0:
            print('Balance cannot be negative..')
            continue

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
            print(f'Account ID {account["id"]} created successfully!')




    # 2. VIEW ACCOUNTS
    elif choice == '2':
        if not accounts:
            print("No accounts found")
            continue

        print(f"\nTotal Accounts: {len(accounts)}")
        print("\n========== Accounts List ==========\n")

        for index, account in enumerate(accounts, start=1):
            print(f"Account #{index}")
            print("------------------------------------------")
            print(f"Account ID   : {account['id']}")
            print(f"Name         : {account['name']}")
            print(f"Age          : {account['age']}")
            print(f"Phone Number : {account['phone_no']}")
            print(f"Balance      : ₹{account['balance']:.2f}")
            print("------------------------------------------\n")




    # 3. SEARCH ACCOUNTS
    elif choice == '3':

        if not accounts:
            print('No accounts found')
            continue

        try:
            search_id = int(input("Enter Account ID to search: "))
        except ValueError:
            print('\nError: Please enter valid numeric Account IDs.')
            continue

        found = False

        for account in accounts:
            if account['id'] == search_id:
                print('\nAccount Details\n')
                print("------------------------------------------")
                print(f"Account ID   : {account['id']}")
                print(f"Name         : {account['name']}")
                print(f"Age          : {account['age']}")
                print(f"Phone Number : {account['phone_no']}")
                print(f"Balance      : ₹{account['balance']:.2f}")
                print("------------------------------------------\n")
                found = True
                break

        if not found:
            print('\nAccount not found\n')

    # 4. UPDATE ACCOUNT
    elif choice == "4":

        if not accounts:
            print("No accounts found.")
            continue

        # Validate ID
        try:
            update_id = int(input("Enter Account ID to update: "))
        except ValueError:
            print("Account ID must be an integer.")
            continue

        found = False

        for account in accounts:
            if account["id"] == update_id:

                print("------------------------------------------")
                print(f"Account ID   : {account['id']}")
                print(f"Name         : {account['name']}")
                print(f"Age          : {account['age']}")
                print(f"Phone Number : {account['phone_no']}")
                print(f"Balance      : ₹{account['balance']:.2f}")
                print("------------------------------------------\n")

                # Validate Name
                name = input("Enter new name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue

                # Validate Age
                try:
                    age = int(input("Enter new age: "))
                except ValueError:
                    print("Age must be an integer.")
                    continue

                # Prevent zero or negative age
                if age <= 0:
                    print("Age must be greater than zero.")
                    continue

                if age > 120:
                    print("Age must be 120 or less.")
                    continue

                # Validate Phone number
                phone_no = input("Enter your phone number: ").strip()

                if not phone_no:
                    print("Phone number cannot be empty.")
                    continue

                if not phone_no.isdigit():
                    print("Phone number must contain digits only.")
                    continue

                if len(phone_no) != 10:
                    print("Phone number must contain exactly 10 digits.")
                    continue


                # Update Account
                account["name"] = name
                account["age"] = age
                account["phone_no"] = phone_no

                save_accounts()

                print(f'Account ID {account["id"]} updated successfully!')
                found = True
                break

        if not found:
            print("Account not found.")



    # 5. DEPOSIT MONEY
    elif choice == '5':

        if not accounts:
            print('No accounts found')
            continue

        try:
            deposit_id = int(input("Enter Account ID: "))
        except ValueError:
            print('\nError: Please enter valid numeric Account IDs.')
            continue

        found = False

        for account in accounts:
            if account["id"] == deposit_id:
                found = True

                try:
                    deposit_amount = float(input("Enter deposit amount: "))
                except ValueError:
                    print('\nError: Please enter valid numeric Amount.')
                    continue

                if deposit_amount <= 0:
                   print('\nInvalid deposit amount')
                else:
                   account["balance"] += deposit_amount
                   print("\nDeposit Successful!")
                   print(f"Deposited Amount : ₹{deposit_amount:.2f}")
                   print(f"Account ID       : {account['id']}")
                   print(f"New Balance      : ₹{account['balance']:.2f}")
                   save_accounts()
                   break

        if not found:
            print("Account not found")


    # 6. WITHDRAW MONEY
    elif choice == '6':

        if not accounts:
            print('No accounts found')
            continue

        try:
            withdraw_id = int(input('Enter Account ID: '))
        except ValueError:
            print('\nPlease enter valid numeric Account IDs.')
            continue

        found = False

        for account in accounts:
            if account["id"] == withdraw_id:
                found = True

                try:
                    withdraw_amount = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print('\nError: Please enter valid numeric Amount.')
                    continue

                if  withdraw_amount <= 0:
                    print('\nInvalid withdrawal amount')

                elif withdraw_amount > account["balance"]:
                    print("\nInsufficient balance!")
                    print(f"Current Balance: ₹{account['balance']:.2f}")

                else:
                    account["balance"] -= withdraw_amount
                    print("\nWithdrawal Successful!")
                    print(f"Withdrawn Amount : ₹{withdraw_amount:.2f}")
                    print(f"Account ID       : {account['id']}")
                    print(f"Remaining Balance: ₹{account['balance']:.2f}")
                    save_accounts()
                    break

        if not found:
            print("Account not found")



    # 7. TRANSFER MONEY
    elif choice == '7':

        if not accounts:
            print('No accounts found')
            continue

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
            print(f"From Account       : {sender_id}")
            print(f"To Account         : {receiver_id}")
            print(f"Sender Balance     : ₹{sender_account['balance']:.2f}")
            print(f"Receiver Balance   : ₹{receiver_account['balance']:.2f}")
            print("===========================================")


    # 8. CHECK BALANCE
    elif choice == "8":

        if not accounts:
            print("No accounts found.")
            continue

        try:
            balance_id = int(input("Enter Account ID: "))
        except ValueError:
            print("Account ID must be an integer.")
            continue

        found = False

        for account in accounts:
            if account["id"] == balance_id:
                print("\n====== Account Balance ======\n")
                print(f'Account ID : {account["id"]}')
                print(f'Name       : {account["name"]}')
                print(f'Balance    : ₹{account["balance"]:.2f}')
                print("\n=============================\n")
                found = True
                break

        if not found:
            print('\nAccount not found\n')


    # 9. DELETE ACCOUNT
    elif choice == "9":

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
                confirm = input("Are you sure you want to delete this account? (Y/N): ").strip().upper()

                if confirm != "Y":
                    print("Deletion cancelled.")
                    continue

                accounts.remove(account)
                print(f'Account {account["id"]} deleted successfully!')
                save_accounts()
                found = True
                break

        if not found:
            print("Account not found.")

    # 10. TOTAL ACCOUNTS
    elif choice == "10":

        if not accounts:
            print('No accounts found')
            continue

        total_money_in_bank = 0

        for account in accounts:
            total_money_in_bank += account["balance"]

        print("\n========== Bank Statistics ==========\n")
        print(f"Total Accounts      : {len(accounts)}")
        print(f"Total Money in Bank : ₹{total_money_in_bank:.2f}")
        print("\n=====================================\n")

    # 11. EXIT
    elif choice == "11":
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice.")
        print("Please enter a number between 1 and 11.")



