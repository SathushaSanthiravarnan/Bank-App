def get_customer_info():
    name = input("Enter customer's name :")
    age = input("Enter customer's age :")
    birthdate = input("Enter customer's birthdate :")
    address = input("Enter customer's address :")
    NIC = input("Enter Customer's NIC :")
    status = input("Enter customer's status (single or married) :")
    user_name = input("Enter the username :")
    password = input("Enter the password with 8 characters :")
    
    return [name, age, birthdate, address, NIC, ststus, user_name, password]


def create_customer_and_user():  
    Customers = get_customer_info()

    with open('customer.txt', 'a') as customers_file, open('user.txt', 'a') as users_file:
        customer_file.write(f'{Customers[0]}, {customers[1]}, {customers[2]}, {customers[3]}, {customers[4]}, {customers[5]}\n')
        user_file_write(f'{customers[6]}, {customers[7]}')
create_customer_and_user()

# testing






