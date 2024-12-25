#from abc import ABC, abstractmethod

# Abstract Base Class
class Animal():
    #@abstractmethod
    def sound(self):
        pass  # Abstract method, no implementation

    def sleep(self):
        print("This animal sleeps.")  # Concrete method

    def move(self):
        pass

# Concrete Classes
class Dog(Animal):
    def sound(self):
        return "Bark"
    def move(self):
        return "Runs fast"

class Cat(Animal):
    def sound(self):
        return "Meow"
    def move(self):
        return "Climbs fast"

# Using the classes
dog = Dog()
cat = Cat()

print(f"Dog: {dog.sound()}")
print(f"Dog Move: {dog.move()}")
print(f"Cat: {cat.sound()}")
print(f"Cat Move: {cat.move()}")
dog.sleep()
cat.sleep()