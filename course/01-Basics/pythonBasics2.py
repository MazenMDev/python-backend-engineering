# Ternary operator
is_friend = True
is_user = True
can_message = "you are my friend" if is_friend else "you are my enemy"
print(can_message)

if is_friend and is_user:
  print("best friend ever")

if is_friend or is_user:
  print("you did it")


print("#"*20)
is_magicion = True
is_expert = False

if is_magicion and is_expert:
  print("you are a master magicion")

elif is_magicion and not(is_expert):
  print("at least you're getting there")

elif not(is_magicion):
  print("you need magic power")

print(True == 1) # true
print('' == 1) # false
print([] == 1) # false
print(10 == 10.0) # true
print([] == []) # true

print("%"*30)
user = {
  'name': 'Golem',
  'age': 5006,
  'can_siwm': False
}

for key, value in user.items():
  print(key, value)

my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for number in my_list:
  total += number
print(total)

for _ in range(10):
  print("hi")

for i, char in enumerate("Hello"):
  print(i, char)


# Exercise
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
counter = 0
while counter < len(picture):
  for pixel in picture[counter]:
    if pixel: print('*', end='')
    else: print(' ', end='')
  print(' ')
  counter += 1


# Exercise
some_list = ['a','b','c','b','c','d','m','n','n']
for char in some_list:
  skipFirst = True
  for restChar in some_list:
    if char == restChar and skipFirst:
      skipFirst = False
      continue
    elif char == restChar:
      some_list.remove(restChar)
print (some_list)


# paramaters
def say_hello(name, mood):
  print(f"Hello {name}, {mood}")

# positional arguments
say_hello('mazen', 'happy')
# keyword arguments
say_hello(mood='happy', name='mazen')

def total(num1, num2):
  def another_func(num1, num2):
    return num1 + num2
  return another_func(num1, num2)

print(total(10, 20))


def checkDriverAge(age = 0):
  if int(age) < 18:
    print("sorry")
  elif int(age) > 18:
    print("go")
  elif int(age) == 18:
    print("congrats")
checkDriverAge(92)


def test(a):
  """
  Info: this function tests and prints param a
  """
  print(a)

test('?')
help(test)
print(test.__doc__)

def super_func(*args, **kwargs):
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))
#rule: params, *args, default params, **kwargs

def highest_even(li):
  highest = 0
  for item in li:
    if item % 2 == 0:
      highest = max(item, highest)
  return highest

print(highest_even([10,2,3,4,8,11]))

# note: we can use max(list)


a = "helllloooo"

if((n := len(a)) > 8):
  print(f"too long {n} characters")

while ((n := len(a)) < 1):
  print(n)
  a = a[:-1]
print(a)


total: int = 0
def count():
  global total
  total += 1
  return total


count()
count()
count()
print(count())


def outer():
  x = "local"
  def inner():
    nonlocal x
    x = "nonlocal"
    print("inner: ", x)

  inner()
  print("outer: ", x)

outer()

