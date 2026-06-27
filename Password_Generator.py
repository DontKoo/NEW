import random

elements = "+-/!@#$%^&*()_+=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Podaj dlugosc hasla: "))
password = ""

for i in range(length):
    password += random.choice(elements)

print(password)
