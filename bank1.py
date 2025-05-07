import os
import random

# Function to collect customer information
def get_customer_info():
    name = input("Enter customer's name: ")
    age = input("Enter customer's age: ")
    birthdate = input("Enter customer's birthdate: ")
    address = input("Enter customer's address: ")
    NIC = input("Enter customer's NIC: ")
    status = input("Enter customer's status (single or married): ")
    user_name = input("Enter the username: ")
    password = input("Enter the password (8 characters): ")
    
    return {
        "Name": name,
        "Age": age,
        "Birthdate": birthdate,
        "Address": address,
        "NIC": NIC,
        "Status": status,
        "User_name": user_name,
        "Password": password
    }

# Function to generate customer ID
def Customer_id():
    if not os.path.exists('customer.txt') or os.path.getsize('customer.txt') == 0:
        return "C0001"
    
    with open('customer.txt', 'r') as customers_file:
        last_line = customers_file.readlines()[-1]  # Read last line
        last_id = int(last_line.split(',')[0][1:])  # Extract numeric part
        return f"C{last_id + 1:04}"  # Format as C000X

# Function to generate user ID
def User_id():
    if not os.path.exists('user.txt') or os.path.getsize('user.txt') == 0:
        return "U0001"
    
    with open('user.txt', 'r') as users_file:
        last_line = users_file.readlines()[-1]  # Read last line
        last_id = int(last_line.split(',')[0][1:])  # Extract numeric part
        return f"U{last_id + 1:04}"  # Format as U000X

# Function to create admin user if user file is empty
def create_admin_user():
    if not os.path.exists('user.txt') or os.path.getsize('user.txt') == 0:
        with open('user.txt', 'a') as user_file:
            admin_id = User_id()            
            admin_username = "admin"
            admin_password = "sathu"            
            user_file.write(f"{admin_id},{admin_username},{admin_password},Admin\n")            
        print("Admin user created successfully with username 'admin' and password 'sathu'.\n")

create_admin_user()

# Function to create customer and user entries
def create_customer_and_user():  
    customers = get_customer_info()
    with open('customer.txt', 'a') as customers_file, open('user.txt', 'a') as users_file:
        customer_id = Customer_id()
        user_id = User_id()
        customers_file.write(f'{customer_id},{customers["Name"]},{customers["Age"]},{customers["Birthdate"]},{customers["Address"]},{customers["NIC"]},{customers["Status"]}\n')
        users_file.write(f'{user_id},{customers["User_name"]},{customers["Password"]},Customer\n')

create_customer_and_user()

# Function to generate a random account number
def create_account_number():
    return str(random.randint(1000000000, 9999999999))  # Generates a 10-digit account number

# Function to create an account and store in file
def create_account():  
    account_number = create_account_number()
    user_id = User_id()  # Ensure correct function call
    
    with open('accounts.txt', 'a') as accounts_file:
        accounts_file.write(f'{user_id},{account_number}\n')

create_account()

balance = 0
def deposit_money():
    global amount
    while True:
        try:
            deposit_amount = float(input("Enter your deposit money :"))
            balance += deposit_amount
            print("'Successfully You Deposit Your Money...!' Your New Balance is:", balance)
            break

        except ValueError:
            print("Enter Number Only...!")

def withdraw_money():



            
            