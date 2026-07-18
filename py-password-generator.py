import random, string
password =''.join(random.choice(string.ascii_letters+string.digits) for i in  range(8)) # Alphanumeric 8 chars
print("Your secure password:")
print(password)