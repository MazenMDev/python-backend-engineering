class User(object):
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power {self.power}")


class Archer(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power {self.power}")


wizard1 = Wizard("tester1", 45)
# wizard1.attack()

archer1 = Archer("tester2", 30)

for char in [wizard1, archer1]:
    char.attack()