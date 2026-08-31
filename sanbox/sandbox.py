# class Account:
#     def __init__(self, owner, balance=0.0):
#         self.__balance = balance


# acc = Account("Mazen", 1000)
# acc.__balance = 999999  # does this touch the real balance?
# print(acc._Account__balance)  # what does THIS print?
# acc._Account__balance = 9023432047
# print(acc._Account__balance)


class Account2:
    def __init__(self, owner, balance=0.0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def Error():
        pass

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise WithdrawLimitError(
                f"Withdrawal of {amount:.2f} exceeds available balance of {self._balance:.2f}"
            )
        self._balance -= amount


class WithdrawLimitError(Exception):
    pass


acc2 = Account2("Mazen", 1000)
print(acc2.balance)
acc2.withdraw(250)
print(acc2.balance)
acc2.deposit(500)
print(acc2.balance)
try:
    acc2.withdraw(2000)  # bigger than the balance — on purpose
except WithdrawLimitError as e:
    print(f"you have passed the limit {e}")
print(acc2.balance)

# result_ok = acc2.withdraw(50)  # succeeds
# result_fail = acc2.withdraw(2000)  # fails — bigger than balance
# print(result_ok)
# print(result_fail)


class PlayList:
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    @property
    def songs(self):
        return self._songs.copy()


playList = PlayList()
playList.add("Song A")
playList.add("Song B")

print(playList.songs)
stolen = playList.songs
stolen.append("Song C")

print(stolen)
print(playList.songs)

from abc import ABC, abstractmethod


class Account3(ABC):
    @property
    @abstractmethod
    def account_type(self) -> str:
        pass

    @abstractmethod
    def _can_withdraw(self, amount) -> bool:
        pass


try:
    print(Account3())
except TypeError as e:
    print(f"Can't do that: {e}")


class SavingsAccount(Account3):
    @property
    def account_type(self):
        return "SavingsAccount"

    def _can_withdraw(self, amount):
        return amount <= 100


savingsAccount = SavingsAccount()
print(savingsAccount.account_type)
print(savingsAccount._can_withdraw(70))


import json
from datetime import datetime

# task 1
d = {"year": 2026}
print(type(d["year"]))
json.dump(d, open("test.json", "w"))
loaded = json.load(open("test.json"))
print(type(loaded["year"]))

# task 2
when = datetime.now()
as_string = when.isoformat()
print(type(as_string))  # str, before writing

bad = {"when": as_string}
json.dump(bad, open("test2.json", "w"))

loaded2 = json.load(open("test2.json"))
restored = datetime.fromisoformat(loaded2["when"])
print(type(restored))  # back to datetime, after loading
print(restored)
