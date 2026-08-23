# print("here we go")
# name = input("Enter your name please\n")
# print("Your name sir is: " + name)

# Fundamentals Data types
int
float
str
bool
list
tuple
set
dict

print(2**3)
print(5 // 4)
print(6 % 4)

print(bin(5))
print(int("0b101", 2))

long_strings = """
WOW
ooo
---
"""
print(long_strings)
print("your number is: " + str(100))

print("it's cold")
print('\tit\'s "kind of" cold\n')

name = "mazen"
age = 19
print(f"hello {name}, you are {age} years old")  # formatted strings

selfish = "01234567"
print(selfish[0])
# start:stop:stepover
print(selfish[0 : len(selfish) : 2])
print(selfish[0:2])
print(selfish[::-1])


quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find("be"))
print(quote.replace("be", "me"))

# birth_year = input("What year were you born\n")
# age = 2026 - int(birth_year)
# print(f"Your age is {age}")

# password = input("scecret: ")
# username = input("username: ")
# star_password = "*" * len(password)
# print(f"{username}, your password {star_password} is {len(password)} letters long")

amazon_carts = ["notebooks", "sunglasses", "toys", "grapes"]
print(amazon_carts[0:2])

amazon_carts[0] = "laptop"
new_carts = amazon_carts[:]  # copy
new_carts[0] = "gum"
print(new_carts)
print(amazon_carts)
print("*" * 10)  # -*******
new_carts = amazon_carts  # new_carts pointing on amazon_carts now
print(new_carts)
print(amazon_carts)
print("-" * 10)  # --------
new_carts[0] = "gum"
print(new_carts)
print(amazon_carts)
