# In Constructor use [ __init__(self):] method

# class School:
#     def __init__(self,boys,girls):
#         print("11th Student details:")
#         self.boys=boys
#         self.girls=girls
#     def std_11(self):
#         print("Total Boys =",self.boys,"Total Girls=",self.girls)
#
#
#     boys1=29
#     girls1=30
#
#     def std_12(self):
#         print("12th Student Details:")
#         print("Total Boys =",self.boys1,"Total Girls = ",self.girls1)
#
#
#
# obj=School(45,78)
# obj.std_11()
# obj.std_12()


# class Car:
#     name = None
#     make = None
#     model = None
#
#     def __init__(self, o_name, o_make, o_model):  # Special F(n), called Object is created!
#         self.name = o_name
#         self.make = o_make
#         self.model = o_model
#
#     def start_engine(self):
#         print("Starting a car with the name " + self.name)
#         print("Starting a car with the make " + self.make)
#         print("Starting a car with the model " + self.model)
#
#
# lambo = Car("lambo", "V2", "2024")
# lambo.start_engine()
#
# print(" -- ---- ")
#
# xuv = Car("XUV", "V6", "2023")
# xuv.start_engine()


#--------------------------------------------------


# Web Automation - Selenium

# Page - You are going automate

# class VWOLoginPage:
#     email = None
#     password = None
#
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#
#     def loginconfirm(self):
#         if self.password == "Pass123":
#             print("You are allowed to enter")
#         else:
#             print("Invalid user")
#
#
# obj = VWOLoginPage("amit@amit.com", "123")
# obj.loginconfirm()
#
# print(" ------")
#
# obj1 = VWOLoginPage("pramod@pramod.com", "Pass123")
# obj1.loginconfirm()
#
# print(id(obj))        # this is show memory location id
# print(id(obj1))



# class Computer:
#     def __init__(self,user,password):
#         self.user=user
#         self.password=password
#
#     def my_computer(self):
#         if self.password=="Pawan123":
#             print("Computer Unlock")
#         else:
#             print("invalid user")
#
# obj=Computer("Pawan","Pawan123")
# obj.my_computer()


