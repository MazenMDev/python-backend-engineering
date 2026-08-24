# print("here we go")
# name = input("Enter your name please\n")
# print("Your name sir is: " + name)

# Fundamentals Data types
# int
# float
# str
# bool
# list
# tuple
# dict
# set

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

# List Methods
basket = [1, 2, 3, 4, 5]
new_list = basket.append(100)
basket.insert(4, 100)  # index, object
basket.extend([100])
basket.pop(1)  # index
basket.remove(3)  # value

another_basket = ["a", "b", "c", "d", "e", "d"]
# print(another_basket.sort()) # .sort change in place
print(sorted(another_basket))  # sorted produces a new array
print(another_basket)

print(list(range(101)))

sentence = " "
new_sentence = sentence.join(["hi", "my", "name", "is", "mazen"])
print(new_sentence)

# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

# Dictionary
dictionary = {
  'a' : [1,2,3],
  'b' : 'hello',
  'c': True,
  123: 'test_1',
  True: 'test_2',
}
# the key should be something immutable
print(dictionary['a'][2])

user = {
  'basket' : [1,2,3],
  'greet' : 'hello',
  'age': 20
}

print(user.get('age', 55)) # if you didn't find key 'age' then add the default value 55
print(user.update({'age' : 100}))
print(user.pop('age'))
print(user.popitem())
print(user.clear())


# Tuple
my_tuple = (1,2,3,4,5,5) # it's immutable
print(5 in my_tuple)

print(my_tuple.count(5))
print(my_tuple.index(5))

# Set
my_set = {1,2,3,4,5}
print(my_set)

print("#" * 10)
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
# print(my_set.difference_update(your_set))
# print(my_set)
print(my_set.intersection(your_set))
print(my_set.union(your_set))
print(my_set.isdisjoint(your_set))

small_set = {4,5}
print(small_set.issubset(your_set))
print(your_set.issuperset(small_set))
