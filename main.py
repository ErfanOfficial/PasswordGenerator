import random
import string
import pickle

def generate_password(length, type):

    numbers = string.digits
    letters = string.ascii_letters
    both = string.digits + string.ascii_letters

    if (type == 1):
        password = ""
        for i in range(length):
            password += random.choice(numbers)
    elif (type == 2):
        password = ""
        for i in range(length):
            password += random.choice(letters)
    else:
        password = ""
        password += random.choice(numbers)
        password += random.choice(letters)
        for i in range(length - 2):
            password += random.choice(both)
        password = ''.join(random.sample(password, length))
    return(password)

def get_option():
    option = int(input("Hello, what can I do for you?\n1. Generate password\n2. Display password list\nYour choice: "))
    while(option < 1 or option > 2):
        option = int(input("Please enter a valid value (1 or 2): "))
    return(option)

def save_password():
    save = int(input("Do you want save your password?\n1.YES\n2.NO\nYour choice: "))
    while (save < 1 or save > 2):
        save = int(input("Just enter 1 or 2\nYour choice: "))
    return(save)

option = get_option()

if (option == 1):
    length = int(input("What should be the length of the characters?: "))
    while(length < 2):
        length = int(input("What should be the length of the characters? [You cannot choose a value less than two]: "))

    type = int(input("What should be the character type?\n1.numbers\n2.letters\n3.both\nYour choice: "))

    while (type > 3 or type < 1):
        type = int(input("Incorrect input. Enter true value[1, 2 or 3]\nYour choice: "))

    password = generate_password(length, type)
    print("Your password = %s" %(password))

    save = save_password()

    user_passwords = {}

    if (save == 1):
        pass_name = input("Choose a name for your password: ")
        while(len(pass_name) < 1):
            pass_name = input("The name you choose must have at least 2 characters: ")
        user_name = input("Enter a username: ")
        while(len(pass_name) < 2):
            pass_name = input("The username you choose must have at least 3 characters: ")
        try:
            with open("userpasswords.pkl", 'rb') as f:
                user_passwords = pickle.load(f)
        except FileNotFoundError:
            pass

        user_passwords[pass_name] = {"username":user_name, "password":password}

        with open("userpasswords.pkl", 'wb') as f:
            pickle.dump(user_passwords, f)
        print("Successfully saved")
    else:
        print("Operation cancelled")

else:
    print("Here is the list of passwords you have saved:")
    with open("userpasswords.pkl", 'rb') as f:
        user_passwords = pickle.load(f)
    for i in user_passwords.keys():
        print(i)
    select_password = input("Choose one of the above options: ")
    show_password = user_passwords[select_password]
    print("Name = {}\nUsername = {}\nPassword = {}".format(select_password, show_password["username"], show_password["password"]))
