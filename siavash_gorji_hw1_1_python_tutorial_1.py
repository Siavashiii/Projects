# -*- coding: utf-8 -*-
"""Siavash Gorji - HW1 - 1 - Python Tutorial 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l81o1HId4KFVpWCY9jMrAqHFMOEK9JUU

**Question 1:** Write a Python program that asks the user for their age. If the age is greater than or equal to 18, print "You are an adult." Otherwise, print "You are a minor."
"""

#simple writing code
# Get user input for age
age = int(input("Enter your age: "))

# Check if the user is an adult or a minor
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
###################################################
print("--------------------------")

#Lambda method writing code

# Get user input for age
user_age = int(input("Enter your age: "))

# Check if the user is an adult or a minor
check_age = lambda age: "You are an adult." if age >= 18 else "You are a minor."


# Print the result using the lambda function
print(check_age(user_age))

"""**Question 2:** Write a Python program to print the numbers from 1 to 10 using a for loop."""

# Using a for loop to print numbers from 1 to 10(for loop)

for number in range(1, 11):
    print(number)

###########################################

print("--------------------------")


# Using a for loop to print numbers from 1 to 10(while loop)

number = 1
while number <= 10:
    print(number)
    number += 1

"""**Question 3:** Write a Python program to calculate the sum of all even numbers from 1 to 20 using a while loop."""

# Initialize variable for the sum
sum_of_evens = 0

# Use a for loop to calculate the sum of even numbers from 1 to 20
for number in range(2, 21, 2):
    sum_of_evens += number

# Print the result
print("Sum of even numbers from 1 to 20:", sum_of_evens)


print("--------------------------")


# Initialize variables
number = 1
sum_of_evens = 0

# Use a while loop to calculate the sum of even numbers from 1 to 20
while number <= 20:
    if number % 2 == 0:
        sum_of_evens += number
    number += 1

# Print the result
print("Sum of even numbers from 1 to 20:", sum_of_evens)

"""**Question 4:** Define a function called multiply that takes two parameters and returns their product."""

#use lambda

multiply = lambda x, y: x * y

# Example usage:
result = multiply(2, 6)
print("Product:", result)

########################

#use normal fn

def multiply(x, y):
    """Return the product of two numbers."""
    product = x * y
    return product

# Example usage:
result = multiply(2, 6)
print("Product:", result)

"""**Question 5:** Create a class called Person with a constructor method that initializes the name and age attributes. Then, create an instance of the Person class and print the person's name and age."""

class Person:
    def __init__(self, name, age):
        """Constructor method to initialize name and age attributes."""
        self.name = name
        self.age = age

# Create an instance of the Person class with a different person
another_person1 = Person(name="Siavash Gorji", age=31)
another_person2 = Person(name="Alice", age=25)

# Print the details of the other person
print("Person's Name:", another_person1.name)
print("Person's Age:", another_person1.age)
print("--------------------------")
print("Person's Name:", another_person2.name)
print("Person's Age:", another_person2.age)

"""**Question 6:** Create a subclass called `Student` that inherits from the `Person` class. Add an additional attribute called `student_id` to the `Student` class. Create an instance of the `Student` class and print the student's name, age, and student ID."""

class Person:
    def __init__(self, name, age):
        """Constructor method to initialize name and age atts."""
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        """Constructor method for Student class inheriting from Person."""
        super().__init__(name, age)
        self.student_id = student_id

# Create an instance of the Student class
student_instance1 = Student(name="Siavash", age=31, student_id="67890")
student_instance2 = Student(name="Bob", age=20, student_id="12345")


# Print the student's name, age, and student ID
print("Student's Name1:", student_instance1.name,'|',"Student's Name2:", student_instance2.name)
print("Student's Age1:", student_instance1.age,'|',"Student's Age2:", student_instance2.age)
print("Student ID1:", student_instance1.student_id,'|',"Student ID2:", student_instance2.student_id)

"""**Question 7:** Write a Python program that prompts the user to enter a number and then prints whether the number is prime or not. Create a function called `is_prime` that takes an integer as an argument and returns True if it's prime, and False otherwise."""

is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# Get user input for a number
user_number = int(input("Enter a number: "))

# Check if the entered number is prime and print the result
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

    print("--------------------------")

def is_prime(number):
    #Check if a number is prime
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input for a number
user_number = int(input("Enter a number: "))

# Check if the entered number is prime and print the result
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

"""**Question 8:** Write a Python program that calculates the factorial of a given number using a recursive function. Prompt the user for an integer input and print its factorial."""

def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

    #using while loop
    """
     result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

    """


# Get user input for an integer
user_input = int(input("Enter an integer to calculate its factorial: "))

# Check if the input is a non-negative integer
if user_input < 0:
    print("Please enter a non-negative integer.")
else:
    # Calculate and print the factorial
    result = factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")

"""**Question 9:** Create a class called `Rectangle` with attributes `width` and `height`. Add a method `calculate_area` that calculates and returns the area of the rectangle. Create an instance of the `Rectangle` class and print its area."""

class Rectangle:
    def __init__(self, width, height):
        """Constructor method to initialize width and height atts."""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

# Create an instance of the Rectangle class
rectangle_instance = Rectangle(width=5, height=8)

# Calculate and print the area of the rectangle
area = rectangle_instance.calculate_area()
print("Area of the rectangle:", area)

"""**Question 10:** Create a subclass called `Square` that inherits from the `Rectangle` class. Add a method `calculate_perimeter` to the `Square` class that calculates and returns the perimeter of the square. Create an instance of the `Square` class and print its perimeter."""

class Rectangle:
    def __init__(self, width, height):
        """Constructor method to initialize width and height atts."""
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        """Constructor method for Square class, inheriting from Rectangle."""
        super().__init__(width=side_length, height=side_length)

    def calculate_perimeter(self):
        """Calculate and return the perimeter of the square."""
        return 4 * self.width

# Create an instance of the Square class
square_instance = Square(side_length=4)

# Calculate and print the perimeter of the square
perimeter = square_instance.calculate_perimeter()
print("Perimeter of the square:", perimeter)

"""**Question 11:** Create a base class called `Animal` with attributes `name` and `species`. Provide a constructor to initialize these attributes and a method called `speak` that prints a generic message like "The animal makes a sound."
"""

class Animal:
    def __init__(self, name, species):
        """Constructor method to initialize name and species atts."""
        self.name = name
        self.species = species

    def speak(self):
        """Method to print a generic message."""
        print("The animal makes a sound.")

"""**Question 12:** Create a subclass called `Dog` that inherits from the `Animal` class. Add a constructor to initialize the `name`, `species`, and `breed` attributes specific to dogs. Override the `speak` method in the `Dog` class to print "Woof!"
"""

class Animal:
    def __init__(self, name, species):
        """Constructor method to initialize name and species atts."""
        self.name = name
        self.species = species

    def speak(self):
        """Method to print a generic message."""
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        """Constructor method for Dog class, inheriting from Animal."""
        super(Dog, self).__init__(name=name, species="Dog")
        self.breed = breed

    def speak(self):
        """Override the speak method to print 'Woof!' for dogs."""
        print("Woof!")

"""**Question 13:** Create another subclass called `Cat` that inherits from the `Animal` class. Add a constructor to initialize the `name`, `species`, and `color` attributes specific to cats. Override the `speak` method in the `Cat` class to print "Meow!"
"""

class Animal:
    def __init__(self, name, species):
        """Constructor method to initialize name and species atts."""
        self.name = name
        self.species = species

    def speak(self):
        """Method to print a generic message."""
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        """Constructor method for Dog class, inheriting from Animal."""
        super().__init__(name=name, species="Dog")
        self.breed = breed

    def speak(self):
        """Override the speak method to print 'Woof!' for dogs."""
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        """Constructor method for Cat class, inheriting from Animal."""
        super().__init__(name=name, species="Cat")
        self.color = color

    def speak(self):
        """Override the speak method to print 'Meow!' for cats."""
        print("Meow!")

"""**Question 14:** Create instances of both the `Dog` and `Cat` classes and call their `speak` methods to demonstrate polymorphism."""

dog_instance = Dog(name="Buddy", breed="Golden Retriever")
cat_instance = Cat(name="Whiskers", color="Tabby")

# Call the speak methods to demonstrate polymorphism
dog_instance.speak()  # Output: Woof!
cat_instance.speak()  # Output: Meow!

print('---------------------------')
##################################

# Create a list of animals
animals = [Dog(name="Buddy", breed="Golden Retriever"),
           Cat(name="Whiskers", color="Tabby")]

# Call the speak methods using a loop to demonstrate polymorphism
for animal in animals:
    animal.speak()