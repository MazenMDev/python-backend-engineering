class BigObject:
    pass


obj1 = BigObject()  # instanciate new obj


class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        if not self.is_valid_age(age):
            raise ValueError("Age must be between 1 and 120")
        self.name = name  # class attribute
        self.age = age  # class attribute

    def run(self):
        return self
        print(f"{self.name} is running")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def is_valid_age(age):
        return 0 < age < 120


player1 = PlayerCharacter("mazen", 19)
player2 = PlayerCharacter("tester", 27)

player1.run()
print(player1.membership)
player1.membership = False
print(player1.membership)
print(player2.membership)
player2.run()

player3 = PlayerCharacter.adding_things(6, 5)
print("-" * 5)
print(player3.name)
print(player3.age)
print("-" * 5)

print(PlayerCharacter.is_valid_age(0))  # True or False

# Exercise Cats Everywhere
# Given the below class:


class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat("cat1", 4)
cat2 = Cat("cat2", 9)
cat3 = Cat("cat3", 5)


# 2 Create a function that finds the oldest cat.
def FindOldestCat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
maxAge = FindOldestCat(cat1.age, cat2.age, cat3.age)
print(f"The oldest cat is {maxAge} years old")

print("$" * 20)
