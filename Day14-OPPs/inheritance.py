#  Inheritance

# Single - 80% use that means most of time use single inheritance
# Multiple
# Multi level
# Hybrid
# Hierarchical


#  Single Inheritance ------------------

# class Parent:
#     def myfunction1(self):
#         print("this is parent class")
#
# class Child(Parent):               # here inherit parent class to child class
#     def myfunction2(self):
#         print("this is child class")
#
# obj=Child()
# obj.myfunction1()
# obj.myfunction2()





# class Father:
#     __private_villa = "GOA"
#     gold = 5
#
#     def drive_car(self):
#         print("Lambo")
#
#     def threeBHKFlat(self):
#         print("3BHK Flat")
#
#     def private_vill_access(self, is_my_son):
#         print(self.__private_villa)
#
#
# class Son(Father):
#     pass
#
# pramod = Son()
# print(pramod.gold)
# pramod.drive_car()
# pramod.threeBHKFlat()
# print(pramod.__private_villa)
# pramod.private_vill_access(True)

# mmd = Father()
# mmd.drive_car()
# mmd.threeBHKFlat()
# mmd.gold



#  Multilevel Inheritance -----------------------

# class Grand_Parent:                   # This is Parent Class
#     def myfunction1(self):
#         print("this is Grand Parent Class")
#
# class Parent(Grand_Parent):           # This is Sub Parent Class
#     def myfunction2(self):
#         print("this is Parent class")
#
# class Child(Parent):                     # This is Child Class inherit
#     def myfunction3(self):
#         print("this is Child class")
#
#
# obj=Child()
# obj.myfunction1()
# obj.myfunction2()
# obj.myfunction3()


# class GF:
#
#     def __init__(self):
#         print("Automatically Called when Object is created")
#
#     def home(self):
#         print("5BHK")
#
#
# class Father(GF):
#     def home2(self):
#         print("GOA")
#
#
# class Son(Father):
#     def home3(self):
#         print("Bangalore")
#
#
# pawan = Son()
# pawan.home()
# pawan.home2()
# pawan.home3()



# Multiple Inheritance -------------------------------------------

# class GrandParent:                        # This is Parent Class
#     def myfunction1(self):
#         print("this is grand parent class")
#
# class Parent:                             # This is Parent Class
#     def myfunction2(self):
#         print("this is parent class")
#
# class Child(GrandParent,Parent):              # This is Child Class and inherit both parent class
#     def myfunction3(self):
#         print("this is child class")
#
#
# obj=Child()
# obj.myfunction1()
# obj.myfunction2()
# obj.myfunction3()




# class Father:
#     def father_money(self):
#         return "5"
#
#     def home(self):
#         return "This is from the Father"
#
#
# class Mother:
#     def mother_money(self):
#         return "2"
#
#     def home(self):
#         return "This is from the Mother"
#
#
# # class Son(Father, Mother):
# #     pass
#
# class Son(Mother, Father):
#     def home(self):
#         return "This is from the Son"
#
#
# son = Son()
# # print(Son.mro())                  # MRO - Method Resolution Order
# print(son.father_money())
# print(son.home())
# print(son.mother_money())
# # print(son.home())



# Hierarchical Inheritance ---------------------------------------------------

# class Parent:
#     def myfunction1(self):
#         print("this is Parent class")
#
# class Child1(Parent):
#     def myfunction2(self):
#         print("this is child 1 class")
#
# class Child2(Parent):
#     def myfunction3(self):
#         print("this is child 2 class")
#
# obj=Child1()
# obj.myfunction1()
# obj.myfunction2()
# obj1=Child2()
# obj1.myfunction3()
# obj1.myfunction1()



# class Vehicle:                   # This is Parent Class
#     def info(self):
#         return "This is a vehicle."
#
# class Car(Vehicle):              # This is Child 1 Class  inherit with parent class
#     def info(self):
#         return "This is a car."
#
#
# class Bicycle(Vehicle):         # This is Child 2 Class  inherit with parent class
#     def info(self):
#         return "This is a bicycle."
#
#
# # car = Car()
# # print(car.info())
# # print(Vehicle.info(car))
# # bicycle=Bicycle()
# # print(Bicycle.info(bicycle))
# # print(Vehicle.info(bicycle))



# Hybrid Inheritance  -------------------------------------------------


# class Parent:
#     def myfunction1(self):
#         print("this is parent class")
#
# class Child1(Parent):
#     def myfunction2(self):
#         print("this is child 1 class")
#
# class Child2(Parent):
#     def myfunction3(self):
#         print("this is child 2 class")
#
# class Child3(Child1,Child2):
#     def myfunction4(self):
#         print("this is child 3 class")
#
#
# obj=Child3()
# obj.myfunction1()
# obj.myfunction2()
# obj.myfunction3()
# obj.myfunction4()


# class A:
#     def methodA(self):
#         return "Method A"
#
#
# class B(A):
#     def methodB(self):
#         return "Method B"
#
#
# class C(A):
#     def methodC(self):
#         return "Method C"
#
#
# class D(B, C):
#     def methodD(self):
#         return "Method D"
#
#
# d = D()
# print(d.methodA())
# print(d.methodB())
# print(d.methodC())
# print(d.methodD())
