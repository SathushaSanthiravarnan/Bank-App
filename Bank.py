import os
import random
def get_customer_info():
    name = input("Enter customer's name :")
    age = input("Enter customer's age :")
    birthdate = input("Enter customer's birthdate :")
    address = input("Enter customer's address :")
    NIC = input("Enter Customer's NIC :")
    status = input("Enter customer's status (single or married) :")
    user_name = input("Enter the username :")
    password = input("Enter the password with 8 characters :")
    
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

def Customer_id():
    if not os.path.exists('customer.txt') or os.path.getsize('customer.txt') == 0:
        return "C0001"
    with open('customer.txt', 'r') as customers_file:
        return f"C{int(customers_file.readlines()[-1].split(',')[0][1:]) + 1:04}"        


def User_id():
    if not os.path.exists('user.txt') or os.path.getsize('user.txt') == 0:
        return "U0001"
        
    with open('user.txt', 'r') as users_file:
        return f"U{int(users_file.readlines()[-1].split(',')[0][1:]) + 1:04}"
    
    # User_id = NIC[:5] 
    # print(User_id)



def create_admin_user():
    if not os.path.exists('user.txt') or os.path.getsize('user.txt') == 0:
        with open('user.txt', 'a') as user_file:
            admin_id = User_id()            
            admin_username = "admin"
            admin_password = "sathu"            
            user_file.write(f"{admin_id},{admin_username},{admin_password}\n")            
        print("Admin user created successfully with username 'admin' and password 'sathu'.\n")
      
   
# create_admin_user()

def create_customer_and_user():  
    customers = get_customer_info()
    with open('customer.txt', 'a') as customers_file, open('user.txt', 'a') as users_file:
        customers_file.write(f'{Customer_id()},{customers["Name"]},{customers["Age"]},{customers["Birthdate"]},{customers["Address"]},{customers["NIC"]},{customers["Status"]}\n')
        users_file.write(f'{User_id()},{customers["User_name"]},{customers["Password"]}\n')

  
# create_customer_and_user()




def create_account_number():
    return str(random.randint(1000000000, 9999999999))  # Generates a 10-digit account number

account_number = create_account_number()
# print("Your Account Number:", account_number)

def find_customer(cus_id):    
    found = False
    with open('customer.txt', 'r') as cus_file:
        for line in cus_file:
            if cus_id in line:
                print('Customer found:', line.strip())
                found = True
                break
    if found:
        return found
    else:        
        return found

# find_customer()

def find_existing_account_number():
    while True:
        account_number = create_account_number() #Auto account number        
        with open('accounts.txt', 'r') as account_file:
            for line in account_file:
                if account_number in line:
                    continue
                else:
                    return account_number    


def create_account():      
    account_number = find_existing_account_number() 
    customer_id = input('Enter Customer ID: ') #get customer id
    isCustomer = find_customer(customer_id)
    if isCustomer:
        amount = float(input('Enter Amount: '))
        with open('accounts.txt', 'a') as accounts_file:
            accounts_file.write(f'{account_number}, {amount}, {customer_id}\n')
        print('Account Created Successfully')
    else:
        print('Customer ID not found.')
        
create_account()














