import random
import string
length = int(input("Enter the length of the password: "))
def password(length):
    letters_numbers = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_numbers) for _ in range(length))
password = password(length)
print("Password:", password)
