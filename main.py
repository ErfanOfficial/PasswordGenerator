import random
import string

# Asking the user for the length of the password | از کاربر درخواست می‌کنیم تا طول پسورد را مشخص کند
password_length = int(input("How many characters do you want in your password?: "))

# Asking the user for the type of characters they want in their password | از کاربر درخواست می‌کنیم تا نوع کاراکترهایی که می‌خواهد در پسورد خود داشته باشد را مشخص کند
password_character_type = int(input("Here are the options you have:\n1. Only numbers.\n2. Only letters.\n3. Both numbers and letters\nPlease enter the number of your choice: "))

# Checking if the user's input is valid | بررسی می‌کنیم که آیا ورودی کاربر معتبر است
while(password_character_type < 1 or password_character_type > 3):
        password_character_type = int(input("Invalid input, please enter one of options 1, 2 or 3: "))

# Defining the character sets | تعریف مجموعه‌های کاراکتر
all_characters = string.ascii_letters + string.digits
letters_only = string.ascii_letters
numbers_only = string.digits

# Generating the password based on the user's choice | تولید پسورد بر اساس انتخاب کاربر
if (password_character_type == 1):
    password = ""
    for item in range(password_length):
        password += random.choice(numbers_only)

elif (password_character_type == 2):
    password = ""
    for item in range(password_length):
        password += random.choice(letters_only)

elif (password_character_type == 3):
    password = ""
    password += random.choice(string.ascii_letters)
    password += random.choice(string.digits)
    for item in range(password_length - 2):
        password += random.choice(all_characters)

# Shuffling the characters in the password if the user chose both numbers and letters | اگر کاربر هر دو نوع کاراکتر را انتخاب کرده بود، کاراکترهای پسورد را مخلوط می‌کنیم
if (password_character_type == 3):
    password = ''.join(random.sample(password, len(password)))

# Printing the generated password | چاپ پسورد تولید شده
print(password)
