# Main purpose of object-Oriented Programming is to organize complex systems cleanly and efficiently.
# OOP is a programming paradigm that uses "objects" to design applications and computer programs.
# It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation.
# OOP allows programmers to create objects that can interact with one another, making it easier to manage and maintain code, especially in large and complex applications.

# Core concepts of OOP include:
# 1. Classes and Objects: A class is a blueprint for creating objects. An object is an instance of a class that contains data and methods to manipulate that data.
# 2. Encapsulation: This is the bundling of data and methods that operate on that data within a single unit, or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data.
# 3. Inheritance: This allows a new class to inherit properties and behavior (methods) from an existing class. This promotes code reusability and establishes a natural hierarchical relationship between classes.
# 4. Polymorphism: This allows objects of different classes to be treated as objects of a common superclass. It is the ability of different classes to respond to the same method call in different ways.


# Example of OOP in Python

class Employee:
    
    # constructor method to initialize the object
    def __init__(self, name):
        self.name = name
    
    # work method to simulate employee working
    def work(self):
        print(f"{self.name} is working")
 
# creating an instance of the Employee class
emp = Employee("Mahesh")
emp.work()
