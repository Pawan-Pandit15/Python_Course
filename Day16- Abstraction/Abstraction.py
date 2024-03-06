# There is one abstract class with one abstract method

'''     class Abstractclass:    ---->  This is Abstract class
              def abstract method(self):  ------> This is Abstract method
                 pass  '''

# class RBI:               # Parent class
#     def interest_rate(self):
#         pass
#
# class SBI(RBI):          # child class
#     def interest_rate(self):
#         print("SBI interest rate is 7%")    # here SBI interest rate implement
#
# class HDFC(RBI):          # child class
#     def interest_rate(self):
#         print("HDFC interest rate is 6%")    # here HDFC interest rate implement
#
# obj=SBI()
# obj.interest_rate()
# obj=HDFC()
# obj.interest_rate()


#---------------------------------------------------

# class Animal:
#     def move(self):
#         pass
#
# class Dog(Animal):
#     def move(self):
#         print("I can Bark")
#
# class Snake(Animal):
#     def move(self):
#         print("I can hiss")
#
# obj=Dog()
# obj.move()
# obj=Snake()
# obj.move()


#-------------------------------------------------------

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         pass
#
#
# class Dog(Animal):
#     def sound(self):
#         return "Bow Bow"
#
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow "
#
#
# dog = Dog("Rancho")
# print(dog.sound())
#
# cat = Cat("CAT")
# print(cat.sound())



#-------------------------------------------------------

#
# from abc import ABC, abstractmethod
#
#
# class ATB(ABC):
#
#     @abstractmethod
#     def perform_task1(self):
#         pass
#
#     @abstractmethod
#     def perform_task2(self):
#         pass
#
#
# class Amit(ATB):
#     def perform_task1(self):
#         return "eating"
#
#     def perform_task2(self):
#         return "drinking"
#
#
# amit = Amit()
# amit.perform_task2()
# print(amit.perform_task2())
# amit.perform_task1()
# print(amit.perform_task1())
