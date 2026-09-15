if __name__ == "__main__":
    print("hello world")
    
print("\n============================================================\n")

class Robot:
    pass   # an empty class — valid, but useless on its own

my_robot = Robot()      # my_robot is now an INSTANCE of the Robot class
print(type(my_robot))   # <class '__main__.Robot'>

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name        # instance attribute
        self.battery = battery  # instance attribute

r2 = Robot("R2")
c3 = Robot("C3", battery=50)

print(r2.name, r2.battery)   # R2 100
print(c3.name, c3.battery)   # C3 50

print("\n============================================================\n")

class Robot:
    manufacturer = "Cyberdyne"   # class attribute — shared by ALL robots

    def __init__(self, name):
        self.name = name   # instance attribute — unique per robot

r2 = Robot("R2")
c3 = Robot("C3")
print(r2.manufacturer)   # Cyberdyne
print(c3.manufacturer)   # Cyberdyne — same value, shared

Robot.manufacturer = "Tyrell Corp"   # change it on the CLASS
print(r2.manufacturer)   # Tyrell Corp — every instance sees the update

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def use_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

    def status(self):
        return f"{self.name}: {self.battery}% battery"

r2 = Robot("R2")
r2.use_battery(30)
print(r2.status())   # R2: 70% battery

print("\n============================================================\n")

class BankAccount:
    bank_name = "Python National Bank"   # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

account = BankAccount("Amara", balance=100)
account.deposit(50)
print(account.withdraw(30))            # 120
print(account.owner, account.balance)  # Amara 120

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def use_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

    def status(self):
        return f"{self.name}: {self.battery}% battery"

class CleaningRobot(Robot):   # CleaningRobot INHERITS from Robot
    pass

c1 = CleaningRobot("Roomba")
print(c1.status())   # Roomba: 100% battery — inherited, unchanged

print("\n============================================================\n")

class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery)   # let Robot handle name & battery
        self.dust_capacity = dust_capacity   # new attribute, specific to this subclass
        self.dust_collected = 0

    def clean(self, amount):
        self.dust_collected = min(self.dust_capacity, self.dust_collected + amount)
        self.use_battery(5)

r = CleaningRobot("Roomba", dust_capacity=300)
print(r.name, r.dust_capacity)   # Roomba 300

print("\n============================================================\n")

class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"{self.name}: beep boop."

class ProtocolRobot(Robot):
    def greet(self):   # OVERRIDES the parent's greet()
        return f"{self.name}: Greetings, I am fluent in over six million forms of communication."

robots = [Robot("R2"), ProtocolRobot("C3")]
for bot in robots:
    print(bot.greet())
# R2: beep boop.
# C3: Greetings, I am fluent in over six million forms of communication.

print("\n============================================================\n")

class ProtocolRobot(Robot):
    def greet(self):
        original = super().greet()   # get the parent's greeting first
        return original + " (translation services also available.)"

robots = [Robot("R2"), ProtocolRobot("C3")]
for bot in robots:
    print(bot.greet())
    
print("\n============================================================\n")

# Inheritance: CleaningRobot IS-A Robot
class CleaningRobot(Robot):
    ...

# Composition: Robot HAS-A Battery
class Battery:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.level = capacity

    def use(self, amount):
        self.level = max(0, self.level - amount)

class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = Battery()   # Robot is composed of a Battery, not a subclass of it

r = Robot("R2")
r.battery.use(30)
print(r.battery.level)   # 70

print("\n============================================================\n")

class Duck:
    def speak(self):
        return "Quack!"

class Robot:
    def speak(self):
        return "Beep!"

def make_it_speak(thing):
    return thing.speak()   # doesn't care what class 'thing' is — only that .speak() exists

print(make_it_speak(Duck()))     # Quack!
print(make_it_speak(Robot()))    # Beep! — Robot isn't related to Duck at all, and it still works

# Sometimes you do need to check an object's type deliberately — for validation, or to branch behavior. isinstance() is the right tool, and it respects inheritance (a CleaningRobot instance is also a Robot instance):

class Robot:
    pass

class CleaningRobot(Robot):
    pass

c = CleaningRobot()
print(isinstance(c, CleaningRobot))     # True
print(isinstance(c, Robot))             # True — CleaningRobot IS-A Robot
print(isinstance(c, str))               # False
print(issubclass(CleaningRobot, Robot)) # True — checks the CLASS relationship, not an instance

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def status(self):
        return f"{self.name}: {self.battery}% battery"

class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity
        self.dust_collected = 0

    def clean(self, amount):
        self.dust_collected = min(self.dust_capacity, self.dust_collected + amount)

class SmartCleaningRobot(CleaningRobot):   # grandchild of Robot, child of CleaningRobot
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery, dust_capacity)   # calls CleaningRobot's __init__,
        self.rooms_mapped = []                           # which in turn calls Robot's

    def map_room(self, room_name):
        self.rooms_mapped.append(room_name)

s = SmartCleaningRobot("Roomba X")
s.clean(50)
s.map_room("Kitchen")
print(s.status())          # Roomba X: 100% battery — inherited from Robot, two levels up
print(s.dust_collected)    # 50 — inherited from CleaningRobot, one level up
print(s.rooms_mapped)      # ['Kitchen'] — defined on SmartCleaningRobot itself

print("\n============================================================\n")

class Flyable:
    def fly(self):
        return f"{self.name} takes off!"

class Swimmable:
    def swim(self):
        return f"{self.name} dives in!"

class DroneRobot(Flyable, Swimmable):   # inherits from BOTH
    def __init__(self, name):
        self.name = name

d = DroneRobot("Aqua-Drone")
print(d.fly())    # Aqua-Drone takes off!
print(d.swim())   # Aqua-Drone dives in!

print("\n============================================================\n")

class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):   # lists A before B
    pass

print(C().greet())   # Hello from A — A comes first in the class definition
print(C.__mro__)     # shows the exact lookup order Python will follow
# (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"Robot(name={self.name!r}, battery={self.battery!r})"

r = Robot("R2")
print(r)     # R2 (100% battery) — uses __str__
print([r])   # [Robot(name='R2', battery=100)] — uses __repr__

print("\n============================================================\n")

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    @staticmethod
    def is_valid_name(name):
        return len(name) > 0 and name.isalnum()

    @classmethod
    def from_config(cls, config_dict):
        return cls(config_dict["name"])   # an alternative way to construct a Robot

print(Robot.is_valid_name("R2"))   # True — no instance needed to check this
r = Robot.from_config({"name": "C3"})   # built via the classmethod instead of Robot("C3")
print(r.name, Robot.population)   # C3 1

print("\n============================================================\n")

class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self._battery = battery   # leading underscore: internal storage

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if value < 0:
            value = 0
        if value > 100:
            value = 100
        self._battery = value

r = Robot("R2")
r.battery = 150   # goes through the setter — gets clamped
print(r.battery)  # 100 — accessed like a plain attribute, no parentheses

print("\n============================================================\n")

class Robot:
    def __init__(self, name):
        self.name = name

r1 = Robot("R2")
r2 = Robot("R2")
print(r1 == r2)   # False — different objects in memory, even with the same name

# Defining __eq__ lets you decide what "equal" means for your class:

class Robot:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

r1 = Robot("R2")
r2 = Robot("R2")
print(r1 == r2)   # True — now comparing by name

print("\n============================================================\n")

from abc import ABC, abstractmethod

class Robot(ABC):
    @abstractmethod
    def move(self):
        """Every subclass MUST implement this."""
        pass

class WheeledRobot(Robot):
    def move(self):
        return "Rolling forward"

w = WheeledRobot()
print(w.move())   # Rolling forward

# r = Robot()   # TypeError: Can't instantiate abstract class Robot with abstract method move

print("\n============================================================\n")

def shout(text):
    return text.upper() + "!"

my_func = shout   # no parentheses — we're assigning the FUNCTION itself, not calling it
print(my_func("hello"))   # HELLO!

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(shout, "hi"))   # HI!!

print("\n============================================================\n")

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}!"

print(greet("Amara"))
# Calling greet
# greet finished
# Hello, Amara!

print(greet.__name__)   # wrapper

print("\n============================================================\n")

def make_multiplier(factor):
    def multiply(n):
        return n * factor   # 'factor' is remembered from the enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10 — remembers factor=2
print(triple(5))   # 15 — remembers factor=3, a completely separate "memory"

print("\n============================================================\n")

from functools import wraps

def log_call(func):
    @wraps(func)   # preserves greet's real name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}!"

print(greet.__name__)   # 'greet' — fixed

print("\n============================================================\n")

def factorial(n):
    if n <= 1:                      # base case — stops the recursion
        return 1
    return n * factorial(n - 1)     # recursive case — calls itself with a smaller problem

print(factorial(5))   # 120

print("\n============================================================\n")

def countdown(n):
    while n > 0:
        yield n   # pauses here, hands back n, and resumes right after on the next call
        n -= 1

for number in countdown(3):
    print(number)
# 3
# 2
# 1

# Calling a generator function doesn't run its body immediately — it returns a generator object that runs lazily, one step per iteration:

gen = countdown(3)
print(gen)         # <generator object countdown at 0x...>
print(next(gen))   # 3 — runs up to the first yield
print(next(gen))   # 2 — resumes right where it left off

print("\n============================================================\n")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("This runs only if NO exception occurred")
finally:
    print("This always runs, error or not")
# Can't divide by zero
# This always runs, error or not

print("\n============================================================\n")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by zero"
    except TypeError:
        return "Both arguments must be numbers"

print(safe_divide(10, 0))     # Can't divide by zero
print(safe_divide(10, "x"))   # Both arguments must be numbers

# If two exception types should be handled identically, catch them together in one clause using a tuple, rather than repeating the same handling code twice:

def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "Invalid division"
    
print(safe_divide(10, 0))     # Invalid division
print(safe_divide(10, "x"))   # Invalid division

print("\n============================================================\n")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Transaction failed: {e}")
# Transaction failed: Insufficient funds

print("\n============================================================\n")

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        message = f"Tried to withdraw {amount} but balance is only {balance}"
        super().__init__(message)
        # super().__init__(f"Tried to withdraw {amount} but balance is only {balance}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(e)
    print(e.amount)   # you can still access the extra data you attached
# Tried to withdraw 500 but balance is only 100
# 500

print("\n============================================================\n")

# try:
#     withdraw(100, 500)
# except InsufficientFundsError as e:
#     print("Logging the error before re-raising...")
#     raise   # re-raises the SAME exception, unchanged

# Or wrap a low-level exception in a more meaningful one, while preserving the original as context:

# try:
#     balance = int("not a number")
# except ValueError as original_error:
#     raise RuntimeError("Failed to process account balance") from original_error
# the traceback will show both errors, with a note that the second was
# "the direct cause" of the first — very useful for debugging

print("\n============================================================\n")

# the manual way
f = open("notes.txt", "w")
try:
    f.write("hello")
finally:
    f.close()   # you have to remember this, even if writing failed

# the idiomatic way
with open("notes.txt", "w") as f:
    f.write("hello")
# f is automatically closed when the block ends, even if an error occurred inside it

print("\n============================================================\n")

def calculate_average(nums):
    assert len(nums) > 0, "Can't average an empty list"
    return sum(nums) / len(nums)

# calculate_average([])   # AssertionError: Can't average an empty list

print("\n============================================================\n")

# LBYL — check first, then act
# if "key" in my_dict:
#     value = my_dict["key"]
# else:
#     value = None

# EAFP — just try it, and handle the failure if it happens
# try:
#     value = my_dict["key"]
# except KeyError:
#     value = None

print("\n============================================================\n")

import logging
logging.basicConfig(level=logging.INFO)

def withdraw(balance, amount):
    if amount > balance:
        logging.error(f"Withdrawal of {amount} exceeds balance of {balance}")
        raise ValueError("Insufficient funds")
    logging.info(f"Withdrew {amount}, new balance: {balance - amount}")
    return balance - amount

withdraw(100, 500)
# ERROR:root:Withdrawal of 500 exceeds balance of 100
# (then the ValueError is still raised as normal — logging doesn't replace exception handling)

print("\n============================================================\n")

print("hello world")