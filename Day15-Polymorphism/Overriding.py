# Method Overriding
# Method Overriding is the runtime polymorphism
# Method Overriding means having same name method, but into different class, and argument are also same
# In method Overriding inheritence is complusary

# child always overide the parent functions
# super means call my parent function

# Method overriding is same like Multilevel Inheritance

# class M1:                      # Parent class no use super method
#     def myfunction(self,a):
#         print("Class m1 function is called")
#
# class M2(M1):
#     def myfunction(self,a):
#         print("Class m2 function is called")
#         super().myfunction(10)
#
# class M3(M2):
#     def myfunction(self,a):
#         print("Class m3 function is called")
#         super().myfunction(10)    # here super function use complusary in overriding
#                                   # when use super function call there upside function
# obj=M3()
# obj.myfunction(10)



#-----------------------------------------------------------------

# class Animal:
#
#     def __init__(self):
#         pass
#
#     def sound(self):
#         print("Animal Sound")
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         pass
#
#     def sound(self):
#         super().sound()
#         print("Dog Sound")
#

# dog = Dog()
# dog.sound()

