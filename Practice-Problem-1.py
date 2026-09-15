"""
Scenario: A small library wants to track book loans. A Book has a title, isbn, and is_checked_out flag. A Member can borrow(book) and return_book(book). A member cannot borrow a book that's already checked out — attempting to do so should raise a custom BookUnavailableError that includes the book's title in its message.

Task: Implement Book, Member, and the custom exception. Add a __str__ on Book that shows title and availability. Demonstrate: a successful borrow, a successful return, and a failed borrow attempt on an already-checked-out book (catching your custom exception and printing a friendly message instead of a raw traceback). 
"""

class BookUnavailableError(Exception):
    """Custom exception raised when attempting to borrow a checked-out book."""
    def __init__(self, title):
        super().__init__(f"The book '{title}' is currently checked out and unavailable.")

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' (ISBN: {self.isbn}) - Status: {status}"

class Member:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        if book.is_checked_out:
            raise BookUnavailableError(book.title)
        book.is_checked_out = True
        print(f"{self.name} successfully borrowed '{book.title}'.")

    def return_book(self, book):
        book.is_checked_out = False
        print(f"{self.name} successfully returned '{book.title}'.")


# --- Demonstration ---
if __name__ == "__main__":
    b1 = Book("The Hobbit", "978-0345339683")
    alice = Member("Alice")
    bob = Member("Bob")

    print(b1)  # Shows Available
    
    # Successful borrow
    alice.borrow(b1)
    print(b1)  # Shows Checked Out
    
    # Failed borrow attempt
    try:
        bob.borrow(b1)
    except BookUnavailableError as e:
        print(f"Oops! Bob couldn't borrow the book: {e}")
        
    # Successful return
    alice.return_book(b1)
    print(b1)  # Shows Available
    
print("\n============================================================\n")
    
"""
Scenario: You need Circle, Rectangle, and Triangle classes that all support .area() and .perimeter(). Every shape should refuse to be constructed with a non-positive dimension (e.g., negative radius) — raising ValueError with a message that names which dimension was invalid.

Task: Build an abstract base class Shape (using abc.ABC and @abstractmethod) that forces every subclass to implement .area() and .perimeter(). Attempting to instantiate Shape directly should fail. Write a function total_area(shapes: list[Shape]) -> float that sums the area of a list of mixed shape types — this only works cleanly if your polymorphism is done right. 
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"Circle radius must be positive, got {radius}")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError(f"Rectangle width must be positive, got {width}")
        if height <= 0:
            raise ValueError(f"Rectangle height must be positive, got {height}")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        for name, val in [("side_a", side_a), ("side_b", side_b), ("side_c", side_c)]:
            if val <= 0:
                raise ValueError(f"Triangle {name} must be positive, got {val}")
        
        # Validating it can actually form a triangle
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("The given sides cannot form a valid triangle.")
            
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

def total_area(shapes: list[Shape]) -> float:
    """Sums the area of a list of mixed shape types."""
    return sum(shape.area() for shape in shapes)


# --- Demonstration ---
if __name__ == "__main__":
    try:
        bad_circle = Circle(-5)
    except ValueError as e:
        print(f"Validation works: {e}")

    shapes_list = [
        Circle(radius=5), 
        Rectangle(width=4, height=6), 
        Triangle(side_a=3, side_b=4, side_c=5)
    ]
    
    print(f"Total Area: {total_area(shapes_list):.2f}")    
    
print("\n============================================================\n")

"""
Scenario: You're wrapping a flaky internal function unreliable_call() (given to students, randomly raises ConnectionError about 50% of the time) that you don't control. Your job is to call it safely, retrying up to 3 times, and only propagate the error if all 3 attempts fail — logging each failed attempt along the way instead of staying silent.

Task: Write a safe_call(func, max_retries=3) wrapper function (not a decorator) that implements this retry logic using proper try/except, catching only ConnectionError specifically. On final failure, raise a custom AllRetriesFailedError that includes how many attempts were made. 
"""

import random

class AllRetriesFailedError(Exception):
    """Raised when an operation fails after max_retries."""
    def __init__(self, attempts):
        super().__init__(f"Operation failed after {attempts} attempts.")

def unreliable_call():
    """Simulated flaky internal function."""
    if random.random() < 0.5:
        raise ConnectionError("Network timeout.")
    return "200 OK: Data retrieved!"

def safe_call(func, max_retries=3):
    """Safely calls a function, catching ConnectionError and retrying."""
    attempts = 0
    while attempts < max_retries:
        attempts += 1
        try:
            result = func()
            print(f"Success on attempt {attempts}!")
            return result
        except ConnectionError as e:
            print(f"Attempt {attempts} failed with ConnectionError: {e}")
            
    # If the loop finishes without returning, all attempts failed
    raise AllRetriesFailedError(attempts)


# --- Demonstration ---
if __name__ == "__main__":
    print("Testing safe_call:")
    try:
        response = safe_call(unreliable_call, max_retries=3)
        print("Final Result:", response)
    except AllRetriesFailedError as e:
        print(f"Final Result: {e}")
        
print("\n============================================================\n")

"""
Scenario: Every Employee shares a company-wide tax_rate (a class attribute), but each employee has their own name and base_salary (instance attributes). HR wants a net_pay() method per employee, and a way to give every employee a raise at once by changing the tax rate — without touching each employee object individually.

Task: Implement Employee correctly separating class vs. instance attributes (this is a deliberate trap — students who make tax_rate an instance attribute by mistake will not get the "change once, affects everyone" behavior). Add a @classmethod alternative constructor from_dict(cls, data: dict) that builds an Employee from a raw dictionary. Demonstrate that changing Employee.tax_rate changes net_pay() for all existing employee instances. 
"""

class Employee:
    # Class attribute shared by ALL instances
    tax_rate = 0.20  

    def __init__(self, name, base_salary):
        # Instance attributes unique to each object
        self.name = name
        self.base_salary = base_salary

    def net_pay(self):
        # We access the class attribute using self.tax_rate (or Employee.tax_rate)
        return self.base_salary * (1 - Employee.tax_rate)

    @classmethod
    def from_dict(cls, data: dict):
        """Alternative constructor to build an Employee from a dictionary."""
        return cls(name=data["name"], base_salary=data["base_salary"])


# --- Demonstration ---
if __name__ == "__main__":
    emp1 = Employee("Sarah", 100000)
    emp2 = Employee.from_dict({"name": "John", "base_salary": 80000})

    print(f"Initial - {emp1.name} Net Pay: ${emp1.net_pay():.2f}")
    print(f"Initial - {emp2.name} Net Pay: ${emp2.net_pay():.2f}")

    print("\n-- HR lowers the company tax rate from 20% to 10% --\n")
    Employee.tax_rate = 0.10  # Changing the class attribute

    # The same instances now calculate their pay differently without being touched
    print(f"Updated - {emp1.name} Net Pay: ${emp1.net_pay():.2f}")
    print(f"Updated - {emp2.name} Net Pay: ${emp2.net_pay():.2f}")
    
print("\n============================================================\n")

"""
Scenario: You have a working calculate_grade(score: float) -> str function. Your instructor wants every call to it logged — the input score, the output grade, and a timestamp — without modifying the original function's code at all.

Task: Write a decorator @log_grades that wraps any function, printing f"[{timestamp}] called {func.__name__} with {args} -> {result}" before returning the original result unchanged. Use functools.wraps so calculate_grade.__name__ still reports correctly after decoration. Explain (one or two sentences, in a comment) why skipping functools.wraps would have mattered here. 
"""

import functools
from datetime import datetime

def log_grades(func):
    """Decorator that logs inputs, outputs, and timestamps of a function."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp = datetime.now()
        result = func(*args, **kwargs)
        print(f"[{timestamp}] called {func.__name__} with {args} -> {result}")
        return result
    return wrapper

@log_grades
def calculate_grade(score: float) -> str:
    """Calculates a letter grade based on a raw score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

# --- Demonstration & Explanation ---
#
# WHY functools.wraps MATTERS:
# If we skipped `@functools.wraps(func)`, the `calculate_grade` function would 
# permanently take on the name "wrapper" and lose its original docstring. This 
# breaks tools that rely on reading function metadata, like help(), IDE tooltips, 
# and automated documentation generators (like Sphinx).

if __name__ == "__main__":
    # Test the decorator
    grade1 = calculate_grade(95)
    grade2 = calculate_grade(72)
    
    # Prove functools.wraps preserved the function's identity
    print(f"\nFunction name after decoration is still: {calculate_grade.__name__}")
    print(f"Docstring preserved: {calculate_grade.__doc__}")