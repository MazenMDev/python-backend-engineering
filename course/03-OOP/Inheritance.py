class User:
    def __init__(self, name):
        self._name = name

    def sign_in(self):
        print(f"{self._name} logged in")


class Wizard(User):
    wizardCounter = 0

    def __init__(self, name=None):
        if name is None:
            Wizard.wizardCounter += 1
            super().__init__(f"wizard {Wizard.wizardCounter}")


class Archer(User):
    def __init__(self, name="Archer"):
        super().__init__(name)


wizard1 = Wizard()
wizard1.sign_in()

wizard2 = Wizard()
wizard2.sign_in()

wizard3 = Wizard()
wizard3.sign_in()

archer = Archer()
archer.sign_in()
