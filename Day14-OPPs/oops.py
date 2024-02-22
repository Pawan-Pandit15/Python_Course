# Class & Objects in Python
# Class -  Attributes and Behaviour

# Person -> Object Pawan, Basant, Ram


# RailwayForm   ---> Class [blueprint]
# harry --> Pawan ki info wala form --> Object [entity]
# tom --> tom ki info wala form --> Object [entity]
# shubham -- shubham ki info wala form --> Object [entity]
# shubham.changeName("Shubhi")



# class myclass:
#     def myfunction(self):
#         print("Hello myfunction")
#
# m1=myclass()
# m1.myfunction()


# class Cal:
#     def sum(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def mul(self, a, b):
#         return a * b
#
#     def div(self, a, b):
#         return a / b
#
#
# obj= Cal()
# result =obj.sum(3, 4)
# print(result)


# class Mul_param:
#     name = None  # Class Variable
#
#     def print_information(self, first_name, last_name, age):
#         a = 10  # Local Variable
#         print("Your name is ", first_name, last_name, age)
#         print(self.name)
#
#
# obj_ref = Mul_param()
# obj_ref.print_information("Amit", "Sharma", 68)


# class Car:
#     color = None
#     model = None
#
#     def car_details(self):
#         print("Your car details is ", self.color, self.model)
#
#
# car_color = input("Enter you car Color\n")
# car_model = input("Enter you car Model\n")
#
# # car_obj_ref = Car()
# car_obj_ref = Car()
#
# car_obj_ref.color = car_color
# car_obj_ref.model = car_model
#
# car_obj_ref.car_details()


# class Person:
#   name = "Pawan"
#   occupation = "Software Developer"
#   networth = 10
#   def info(self):
#     print(f"{self.name} is a {self.occupation}")
#
#
# a = Person()
# b = Person()
# c = Person()
#
# a.name = "Shubham"
# a.occupation = "Accountant"
#
# b.name = "Nitika"
# b.occupation = "HR"
#
# # print(a.name, a.occupation)
# a.info()
# b.info()
# c.info()



# class Car:
#     color=None
#     model=None
#     year=None
#     def cardetails(self):
#         print("car details are ",self.color,self.model,self.year)
#
# car_color = input("enter car color:")
# car_model = input("enter car model:")
# car_year = input("enter car year:")
#
# car_obj_ref = Car()
# car_obj_ref.color=car_color
# car_obj_ref.model=car_model
# car_obj_ref.year=car_year
# car_obj_ref.cardetails()











