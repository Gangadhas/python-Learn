import random

print("Random Password Generator")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(']
totalChar = int(input("Enter no of Char\n"))
totalLetters = int(input("Enter no of letters\n"))
totalNumbers = int(input("Enter no of Numbers\n"))
totalSymbols = int(input("Enter no of Symbols\n"))

password = []
for i in range(0, totalLetters):
    random_char = random.choice(letters)
    password += random_char
print(password)
for i in range(1, totalNumbers + 1):
    random_char = random.choice(Numbers)
    password += random_char
print(password)
for i in range(1, totalSymbols + 1):
    random_char = random.choice(symbols)
    password += random_char
print(password)
random.shuffle(password)
print(password)

pwd = ""
for i in password:
    pwd += i
print(pwd)


