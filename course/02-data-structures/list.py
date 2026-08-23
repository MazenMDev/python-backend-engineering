fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])

myList = []
myList.append("mazen")
myList.append("mahmoud")
myList.append("gamal")
print(myList)
myList.pop()
print(myList)

# List of numbers
ages = [25, 30, 18, 42]

# List of strings
names = ["Alice", "Bob", "Charlie"]

# Mixed types (yes, this works!)
mixed = [1, "hello", 3.14, True]

# Even lists inside lists!
nested = [[1, 2], [3, 4], [5, 6]]

print(ages[0], names[2], mixed[3], nested[1])

numbers = [1, 2, 3, 4, 5]
print(len(numbers))
print("="*20)
print(3 in numbers)
print(99 in numbers)

for num in numbers:
  print(num)


shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
print(len(shopping_cart))
for item in shopping_cart:
  print(item)

############################################################################
print("="*20, "New", "="*20)
person = {
  "name" : "Mazen",
  "age" : 19,
  "city" : "New York"
}

print(person["name"])
print(person["age"])
print(person["city"])

# Create
user = {}

user["username"] = "John"
user["email"] = "John@example.com"
user["is_active"] = True

print(user)
for key, value in user.items():
  print(f"{key}: {value}")

book = {}
book["title"] = "Python basics"
book["author"] = "John chin su"
book["pages"] = 250
book["available"] = True

print(book["title"])
print(book["author"])
print(book["pages"])

############################################################################

group_a = {1, 2, 3, 4}
group_b = {3, 4, 5, 6}

both = group_a & group_b 
print(both)

combined = group_a | group_b
print(combined)

only_in_a = group_a - group_b
print(only_in_a)

# 1. How many unique email addresses total?
# 2. Which emails are on BOTH lists?
# 3. Which emails are ONLY on list1?
list1 = {"alice@email.com", "bob@email.com", "charlie@email.com"}
list2 = {"bob@email.com", "charlie@email.com", "david@email.com"}

unique_number = len(list1 | list2)
print(unique_number)

both = list1 & list2
print(both)

only_in_list1 = list1 - list2
print(only_in_list1)

############################################################################
# This is a tuple - parentheses ()
coordinates = (40.7128, -74.0060)  # Latitude, Longitude of NYC

print(coordinates[0])
print(coordinates[1])

# Database configuration (shouldn't change while program runs)
DB_config = ("localhost", 5432, "myapp_database")

# RGB color (red, green, blue - fixed values)
red_color = (255, 0, 0)

# Returning multiple values from a function
def get_min_max(numbers):
  return (min(numbers), max(numbers))

min_val, max_val = get_min_max([1, 9, 3, 2, 5, 6])
print(f"Min: {min_val}, Max: {max_val}")  

############################################################################

users_list = []

user1 = {"id": 1, "name": "Alice", "age": 25}
user2 = {"id": 2, "name": "Bob", "age": 30}
user3 = {"id": 3, "name": "Alice", "age": 28}  # Another Alice

# Add to our list
users_list.append(user1)
users_list.append(user2)
users_list.append(user3)
print(users_list)

print(f"Total users: {len(users_list)}")

# Set: Get unique names (no duplicate Alices)
unique_names = set()
for user in users_list: 
  unique_names.add(user["name"])
print(f"Unique names: {unique_names}")

# Tuple: Store user's name and age together (immutable pair)
user_info = (user1["name"], user1["age"])
print(f"User info: {user_info}")

print("="*50)

students = []

student1 = {
  "name" : "Mazen", 
  "grades" : [85, 90, 92],
  "student_id": "S001"
}

student2 = {
    "name": "Bob",
    "grades": [78, 85, 80],
    "student_id": "S002"
}

student3 = {
    "name": "Charlie",
    "grades": [92, 95, 98],
    "student_id": "S003"
}

students.append(student1)
students.append(student2)
students.append(student3)
print(students)

for student in students:
  print(f"Name: {student['name']} and Average grade: {sum(student['grades']) / len(student['grades'])}")

unique_grades = set()
for student in students:
  for grade in student["grades"]:
    unique_grades.add(grade)
    
print(unique_grades)