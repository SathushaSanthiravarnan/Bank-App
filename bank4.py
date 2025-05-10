import os
import random
import datetime

# Generate unique IDs
# def generate_id(file_name, prefix):
#     if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
#         return f"{prefix}0001"
#     with open(file_name, 'r') as file:
#         last_id = file.readlines()[-1].split(',')[0][1:]
#     return f"{prefix}{int(last_id) + 1:04}"

# # Generate unique account number
# def generate_account_number():
#     return str(random.randint(1000000000, 9999999999))  # 10-digit unique number

# # Create admin if not exists
# def create_admin():
#     if not os.path.exists("users.txt"):
#         with open("users.txt", "w") as file:
#             file.write(f"{generate_id('users.txt', 'A')},admin,sathu,admin\n")
#         print("Admin created with default username 'admin' and password 'sathu'.")

# # Register User
# def register_user():
#     username = input("Enter username: ")
#     password = input("Enter password (8 characters): ")
#     role = input("Enter role (user/admin): ")
#     with open("users.txt", "a") as file:
#         file.write(f"{generate_id('users.txt', 'U')},{username},{password},{role}\n")
#     print("User registered successfully!")

# # Login Function
# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     with open("users.txt", "r") as file:
#         for line in file:
#             user_id, stored_username, stored_password, role = line.strip().split(',')
#             if stored_username == username and stored_password == password:
#                 print(f"Login successful! Welcome {role}.")
#                 return role
#     print("Invalid credentials.")
#     return None

# # Create Bank Account
# def create_account():
#     customer_id = generate_id("customers.txt", "C")
#     account_number = generate_account_number()
#     initial_deposit = float(input("Enter initial deposit amount: "))
    
#     with open("customers.txt", "a") as file:
#         file.write(f"{customer_id},{account_number},{initial_deposit}\n")
    
#     print(f"Account created successfully! Your account number: {account_number}")

# # Record transaction
# def record_transaction(account_number, amount, transaction_type):
#     timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
#     with open("transactions.txt", "a") as file:
#         file.write(f"{account_number},{amount},{transaction_type},{timestamp}\n")
#     print(f"{transaction_type} of {amount} recorded successfully!")

# # Deposit Money
# def deposit():
#     account_number = input("Enter your account number: ")
#     deposit_amount = float(input("Enter deposit amount: "))
    
#     with open("customers.txt", "r") as file:
#         lines = file.readlines()
    
#     updated_lines = []
#     found = False
#     for line in lines:
#         customer_id, acc_num, balance = line.strip().split(',')
#         if acc_num == account_number:
#             balance = str(float(balance) + deposit_amount)
#             updated_lines.append(f"{customer_id},{acc_num},{balance}\n")
#             found = True
#         else:
#             updated_lines.append(line)

#     if found:
#         with open("customers.txt", "w") as file:
#             file.writelines(updated_lines)
#         record_transaction(account_number, deposit_amount, "Deposit")
#     else:
#         print("Account not found!")

# # Withdraw Money
# def withdraw():
#     account_number = input("Enter your account number: ")
#     withdraw_amount = float(input("Enter withdraw amount: "))

#     with open("customers.txt", "r") as file:
#         lines = file.readlines()

#     updated_lines = []
#     found = False
#     for line in lines:
#         customer_id, acc_num, balance = line.strip().split(',')
#         if acc_num == account_number and float(balance) >= withdraw_amount:
#             balance = str(float(balance) - withdraw_amount)
#             updated_lines.append(f"{customer_id},{acc_num},{balance}\n")
#             found = True
#         else:
#             updated_lines.append(line)

#     if found:
#         with open("customers.txt", "w") as file:
#             file.writelines(updated_lines)
#         record_transaction(account_number, withdraw_amount, "Withdrawal")
#     else:
#         print("Insufficient balance or account not found!")

# # Transfer Money
# def transfer():
#     sender_acc = input("Enter your account number: ")
#     receiver_acc = input("Enter recipient's account number: ")
#     transfer_amount = float(input("Enter transfer amount: "))

#     with open("customers.txt", "r") as file:
#         lines = file.readlines()

#     updated_lines = []
#     sender_found = False
#     receiver_found = False

#     for line in lines:
#         customer_id, acc_num, balance = line.strip().split(',')
#         if acc_num == sender_acc and float(balance) >= transfer_amount:
#             balance = str(float(balance) - transfer_amount)
#             updated_lines.append(f"{customer_id},{acc_num},{balance}\n")
#             sender_found = True
#         elif acc_num == receiver_acc:
#             balance = str(float(balance) + transfer_amount)
#             updated_lines.append(f"{customer_id},{acc_num},{balance}\n")
#             receiver_found = True
#         else:
#             updated_lines.append(line)

#     if sender_found and receiver_found:
#         with open("customers.txt", "w") as file:
#             file.writelines(updated_lines)
#         record_transaction(sender_acc, transfer_amount, "Transfer to " + receiver_acc)
#         record_transaction(receiver_acc, transfer_amount, "Received from " + sender_acc)
#         print("Transfer successful!")
#     else:
#         print("Invalid account details or insufficient funds.")

# # View Transaction History
# def transaction_history():
#     account_number = input("Enter your account number: ")
#     print(f"Transaction History for Account {account_number}:\n")
#     with open("transactions.txt", "r") as file:
#         for line in file:
#             acc_num, amount, transaction_type, timestamp = line.strip().split(',')
#             if acc_num == account_number:
#                 print(f"{transaction_type}: {amount} on {timestamp}")

# # Main Menu
# def main():
#     create_admin()
    
#     while True:
#         print("\n=== Bank System Menu ===")
#         print("1. Register\n2. Login\n3. Exit")
#         choice = input("> Select an option (1/2/3): ")

#         if choice == "1":
#             register_user()
#         elif choice == "2":
#             role = login()
#             if role == "admin":
#                 while True:
#                     print("\nAdmin Menu: \n1. Create Account\n2. View Transactions\n3. Logout")
#                     admin_choice = input("> Choose option (1/2/3): ")
#                     if admin_choice == "1":
#                         create_account()
#                     elif admin_choice == "2":
#                         transaction_history()
#                     elif admin_choice == "3":
#                         break
#             elif role == "user":
#                 while True:
#                     print("\nUser Menu: \n1. Deposit\n2. Withdraw\n3. Transfer\n4. View Transactions\n5. Logout")
#                     user_choice = input("> Choose option (1/2/3/4/5): ")
#                     if user_choice == "1":
#                         deposit()
#                     elif user_choice == "2":
#                         withdraw()
#                     elif user_choice == "3":
#                         transfer()
#                     elif user_choice == "4":
#                         transaction_history()
#                     elif user_choice == "5":
#                         break
#         elif choice == "3":
#             break

#main()
import os
from datetime import datetime

#==============================================================***ID GENERATOR***===================================================================================================#

def create_customer_next_id():
    if not os.path.exists("customer.txt") or os.path.getsize("customer.txt") == 0:
        return "C001"
    with open("customer.txt", "r") as customer_file:
        return f"C{int(customer_file.readlines()[-1].split(",")[0][1:]) + 1:04}"

def create_user_next_id():
    if not os.path.exists("user.txt") or os.path.getsize("user.txt") == 0:
        return "U001"
    with open("user.txt", "r") as user_file:
        return f"U{int(user_file.readlines()[-1].split(",")[0][1:]) + 1:04}"

#====================================================================***ADMIN***==================================================================================================# 

def create_first_admin():
    if not os.path.exists("user.txt") or os.path.getsize("user.txt") == 0:
        admin_name = "ADMIN"
        admin_password = "Sathu15"
        with open("user.txt", "a") as user_file:
            user_file.write(f"{create_user_next_id()},{admin_name},{admin_password},Admin\n")
        print(f"Admin Login Details: Username: {admin_name}, Password: {admin_password}")

#===================================================================***VALID INPUT***================================================================================================#

def get_valid_input(prompt):
        while True:
            value = input(prompt).strip()
            if value:  # Check if input is not empty
                return value
            else:
                print("Input cannot be empty. Please enter a valid value.")


#=================================================================***CUSTOMER INFOMATION***===========================================================================================# 

def get_customer_info():
    username = get_valid_input("Enter customer's username: ")
    password = input("Enter customer's password: ")
    name = get_valid_input("Enter customer's name: ")
    NIC = get_valid_input("Enter customer's NIC NO: ")
    age = get_valid_input("Enter customer's age: ")
    gender = get_valid_input("Female or Male: ")
    address = get_valid_input("Enter customer's address: ")
    phone = get_valid_input("Enter customer's phone number: ")

    return {
        "username": username,
        "password": password,
        "name": name,
        "NIC_NO": NIC,
        "age": age,
        "gender": gender,
        "address": address,
        "Phone_No": phone
    }

#================================================================***LOGIN SYSTEM***===============================================================================================#

def login_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("user.txt", "r") as user_file:
            for line in user_file:
                fields = line.strip().split(",")
                if len(fields) >= 4 and fields[1] == username and fields[2] == password:
                    print("Login successful!")
                    return fields[3]  # Return role (Admin/Customer)
        print("Login failed. Try again.")
        return None
    except FileNotFoundError:
        print("User file not found.")
        return None

#=================================================================***CREATE CUSTOMER AND USER***===================================================================================# 

def create_customer_and_user():
    customer = get_customer_info()
    with open("customer.txt", "a") as customer_file, open("user.txt", "a") as user_file:
        customer_id = create_customer_next_id()
        user_id = create_user_next_id()
        customer_file.write(f"{customer_id},{customer['name']},{customer['NIC_NO']},{customer['age']},{customer['gender']},{customer['address']},{customer['Phone_No']}\n")
        user_file.write(f"{user_id},{customer['username']},{customer['password']},Customer\n")
        print(f"Customer and user created successfully. Customer ID: {customer_id}, User ID: {user_id}")

#===================================================================***CREATE ACCOUNT***=============================================================================================# 

def create_new_account():
    id_number = input("Enter customer ID number: ")

    found = False
    try:
        with open("customer.txt", "r") as customer_file:
            for line in customer_file:
                if line.startswith(id_number):
                    found = True
                    break
    except FileNotFoundError:
        print("Customer file not found.")
        return

    if not found:
        print("Customer ID not found. Please create customer first.")
        return

    account_num = 1000000
    try:
        with open("accounts.txt", "r") as account_file:
            lines = account_file.readlines()
        count = len(lines)
    except FileNotFoundError:
        count = 0

    new_account_no = account_num + count
    try:
        ac_balance = float(input("Enter your deposit money: "))
        if ac_balance < 1000:
            print("Minimum deposit should be at least 1000.")
            return

        with open("accounts.txt", "a") as account_file:
            account_file.write(f"{id_number},{new_account_no},{ac_balance}\n")

        print(f"New account created successfully! Account Number: {new_account_no}, Balance: {ac_balance}")
    except ValueError:
        print("Invalid input for balance.")

#=====================================================================***BALANCE***==================================================================================================#

def check_balance():
    acc_no = input("Enter your account number: ").strip()
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[1] == acc_no:
                    print(f"Account Number: {acc_no}, Balance: {parts[2]}")
                    return
        print("Account not found.")
    except FileNotFoundError:
        print("Account file not found.")

#=======================================================================***TRANSACTIONS***===========================================================================================# 

def amount_input():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError("Amount must be grater than 0.")
            return amount
        except ValueError:
            print("Invalid input. Try again!!!.")

#==========================================================================***DEPOSIT***=============================================================================================#

def deposit():
    account_number = input("Enter account number: ").strip()
    updated = False
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts[1] == account_number:
                    balance = float(parts[2])
                    deposit_amount = amount_input()
                    new_balance = balance + deposit_amount
                    file.write(f"{parts[0]},{account_number},{new_balance}\n")
                    updated = True

                    timestamp = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
                    with open("transaction.txt", "a") as trans_file:
                        trans_file.write(f"account: {account_number}, deposit: {deposit_amount}, balance: {new_balance}, time: {timestamp}\n")
                    print(f"Deposit successful! New balance: {new_balance}")
                else:
                    file.write(line)

        if not updated:
            print("Account not found.")
    except FileNotFoundError:
        print("accounts.txt not found.")

#========================================================================***WITHDRAW***==============================================================================================#
def withdraw():
    acc_no = input("Enter account number: ").strip()
    updated = False
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts[1] == acc_no:
                    balance = float(parts[2])
                    withdraw_amt = amount_input()
                    if withdraw_amt <= balance:
                        new_balance = balance - withdraw_amt
                        file.write(f"{parts[0]},{acc_no},{new_balance}\n")
                        updated = True

                        timestamp = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
                        with open("transaction.txt", "a") as trans_file:
                            trans_file.write(f"account: {acc_no}, withdraw: {withdraw_amt}, balance: {new_balance} time: {timestamp}\n")
                        print(f"Withdraw successful! New balance: {new_balance}")
                    else:
                        print("Insufficient balance.")
                        file.write(line)
                else:
                    file.write(line)

        if not updated:
            print("Account not found.")
    except FileNotFoundError:
        print("account_no.txt not found.")

#======================================================================***UPDATE***===============================================================================================#

def update_customer():
    customer_id = input("Enter customer ID: ")
    updated = False

    try:
        with open("customer.txt", "r") as file:
            lines = file.readlines()

        with open("customer.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts[0] == customer_id:
                    updated = True
                    print("1. Name\n2. NIC\n3. Age\n4. Gender\n5. Address\n6. Phone")
                    choice = input("Enter field to update: ")

                    if choice == "1":
                        parts[1] = get_valid_input("New name: ")
                    elif choice == "2":
                        parts[2] = get_valid_input("New NIC: ")
                    elif choice == "3":
                        parts[3] = get_valid_input("New age: ")
                    elif choice == "4":
                        parts[4] = get_valid_input("New gender: ")
                    elif choice == "5":
                        parts[5] = get_valid_input("New address: ")
                    elif choice == "6":
                        parts[6] = get_valid_input("New phone: ")

                    file.write(",".join(parts) + "\n")
                else:
                    file.write(line)

        if updated:
            print("Customer updated successfully.")
        else:
            print("Customer ID not found.")

    except FileNotFoundError:
        print("customer.txt not found.")

#=============================================================***TRANSFER MONEY***=================================================================================================#
def transfer_money():
    print("\n*************TRANSFER_MONEY*******************")
    
    from_account_number = input("Enter Your Account Number: ").strip()
    to_account_number = input("Enter transfer Account Number").strip()
    updated = False
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        with open("accounts.txt", "w") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts[1] == from_account_number:
                    balance = float(parts[2])
                    transfer_amount = amount_input()
                    new_balance = balance - transfer_amount
                if parts[1] == to_account_number:   
                    balance = float(parts[2])
                    file.write(f"{parts[0]},{from_account_number},{new_balance}\n")
                    updated = True
                    time_menu = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
                    
                    with open("transaction.txt", "a") as trans_file:
                        trans_file.write(f"from_acc: {from_account_number}, to_acc: {to_account_number}, transfer: {transfer_amount},balance: {new_balance} time: {time_menu}\n")
                    print(f"Transfer Money successful! New balance: {new_balance}")
                else:
                    file.write(line)

        if not updated:
            print("Account not found.")
    except FileNotFoundError:
        print("account_no.txt not found.")

#================================================================***TRANSACTION HISTORY***=========================================================================================#

def transaction_history():
    account_no = input("Enter Your Account Number: ")
    try:
        with open("transaction.txt", "r") as transaction_file:
            print(f"{'account_no':<10}{'current balance':<15}{'Action':<10}{'amount':<15}{'time':}\n")
            for trans_datas_line in transaction_file:
                transaction_data = trans_datas_line.strip().split(',')
                if account_no == transaction_data[0]:
                    print(f"{transaction_data[0]:<10}{transaction_data[1]:<15}{transaction_data[2]:<10}{transaction_data[3]:<15}{transaction_data[4]}\n")
                else:
                    continue

    except FileNotFoundError:
        print("Transaction file not found!!!")    

    


#=====================================================================***ADMIN & CUSTOMER MENU***=================================================================================# 

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Create User")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. View Transaction history")
        print("7. Check Balance")
        print("8. Update Customer")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_customer_and_user()
        elif choice == "2":
            create_new_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            check_balance()
        elif choice == "8":
            update_customer()
        elif choice == "9":
            break
        else:
            print("Invalid input.")

def customer_menu():
    while True:
        print("\nCustomer Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer Money")
        print("4. View Transaction history")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            transfer_money()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            break
        else:
            print("Invalid input.")

#=============================================================***ADMIN OR CUSTOMER OPTION***==========================================================================================#

def select_option_ad_or_cus():
    while True:
    
        print("!!!Select the Role Admin or Customer!!! ")
        print("Enter Number '1' if you are Admin")
        print("Enter Number '2' if you are Customer")
        print("Enter Number '3' if you want Exit")

        select_option = input("Enter a Number '1' or '2' or '3': ")
        
        if select_option == '1':
            admin_menu()
        elif select_option == '2':
            customer_menu()
        elif select_option == '3':
            print("!!!THANK YOU!!!")  
            break
        else:
            print("!!!...Enter Number Only '1' OR '2'...!!!")

#==========================================================================***MAIN***===============================================================================================#

def main():
    create_first_admin()
    select_option_ad_or_cus()
    role = login_system()
    if role == "Admin":
        admin_menu()
    elif role == "Customer":
        customer_menu()

if __name__ == "__main__":
    main()

    
# TRANSACTION MONEY

# def transfer_money():
#     print("\n*************TRASFER_MONEY*******************")
    
#     from_account_number = input("Enter Your Account Number: ").strip()
#     to_account_number = input("Enter transfer Account Number").strip()
#     updated = False
#     try:
#         with open("accounts.txt", "r") as file:
#             lines = file.readlines()

#         with open("accounts.txt", "w") as file:
#             for line in lines:
#                 parts = line.strip().split(",")
#                 if parts[1] == from_account_number:
#                     balance = float(parts[2])
#                     transfer_amount = amount_input()
#                     new_balance = balance - transfer_amount
#                 if parts[1] == to_account_number:   
#                     balance = float(parts[2])
#                     file.write(f"{parts[0]},{from_account_number},{new_balance}\n")
#                     updated = True
#                     time_menu = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
                    
#                     with open("transaction.txt", "a") as trans_file:
#                         trans_file.write(f"from_acc: {from_account_number}, to_acc: {to_account_number}, transfer: {transfer_amount},balance: {new_balance} time: {time_menu}\n")
#                     print(f"Transfer Money successful! New balance: {new_balance}")
#                 else:
#                     file.write(line)

#         if not updated:
#             print("Account not found.")
#     except FileNotFoundError:
#         print("account_no.txt not found.")

# transfer_money()

# # TRANSACTION HISTORY

# def transaction_history():
#     account_no = input("Enter Your Account Number: ")
#     try:
#         with open("transaction.txt", "r") as transaction_file:
#             print(f"{'account_no':<10}{'current balance':<15}{'Action':<10}{'amount':<15}{'time':}\n")
#             for trans_datas_line in transaction_file:
#                 transaction_data = trans_datas_line.strip().split(',')
#                 if account_no == transaction_data[0]:
#                     print(f"{transaction_data[0]:<10}{transaction_data[1]:<15}{transaction_data[2]:<10}{transaction_data[3]:<15}{transaction_data[4]}\n")
#                 else:
#                     continue

#     except FileNotFoundError:
#         print("Transaction file not found!!!")    

    

