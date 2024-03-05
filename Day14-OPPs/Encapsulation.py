# Encapsulation - bind the data v and methods(hide the important variables)
# Data members / Class variable -
# Functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods



# class Car:
#     name = None
#
#     # password = "123"
#     # 3 different tyes of Data Members / class variables
#
#     def __init__(self):
#         self.public_var = "public"  # Public - Anyone can access it
#         self._protected_var = "protected123"
#         self.__private_var = "pass@12"
#         self.__password = "pass@123"
#
#     def _protected_method(self):
#         print("Protected!")
#
#     def __private_method(self):
#         print("Private!")
#         print()
#
#     def printName(self):
#         print("I am allowed to use the private variable becz I am in class " + self.__password)
#
#
# xuv = Car()
# xuv.printName()
# xuv._protected_method()
#
#
# # lambo= Car("Lambo")
# # lambo.printName()
#
# print(xuv.public_var)
# # print(xuv.__password)
# print(xuv.printName())


# class MyClass:
#
#     def __init__(self):
#         self.name = "Amit"
#
#     def public_func(self):
#         print("This is public")
#
#     def __private_func(self):
#         print("This is private")
#
#     def public_fn_private(self):
#         self.__private_func()
#
#
# # Security -> Not everyone can access your variables, f(n)
#
#
# a = MyClass()
# a.public_func()
# # a.__private_func()     #Not allowed,
# a.public_fn_private()




# class Phone:
#     def __init__(self,name):
#         self.name=name
#
#     def public_function(self):
#         print("this is public function")
#         print("this is your name:",self.name)
#
#     def __private(self):
#         print("this is private function you cannot use")
#
#     def _protected(self):
#         print("this is protected function")
#
#     def public_1(self):
#         print("this is again public 1 function")
#
#     def public_call_private(self):      # here change private to public then call
#         self.__private()
#
#
#
#
# obj=Phone("pawan")
# obj.public_function()
# # obj.__private()         # directly cannot call private function
# obj._protected()
# obj.public_1()
# obj.public_call_private()     #  here call private function


# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#         self.__private_var = 100
#
#     def public_fn(self):
#         print(self.__private_var)
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def _withdraw(self, amount):
#         self.balance -= amount
#
#     def __show_balance(self):
#         print("Your Bal", self.balance)
#
#     def if_you_are_auth(self, flag):
#         if flag:
#             self.__show_balance()
#         else:
#             print("Not allowed")
#
#     def do_with_by_bank_manager(self, amount):
#         self._withdraw(amount=amount)
#
#
# jp_chase = BankAccount()
# jp_chase.deposit(1000)
# jp_chase.do_with_by_bank_manager(499)
# jp_chase.if_you_are_auth(False)
# jp_chase.public_fn()


# class Password:
#     def __init__(self, password):
#         self.__password = password
#         self.public_var = 10
#
#     # F(n) and GET and SET
#
#     def get_password(self, is_auth):
#         if is_auth:
#             print(self.__password)
#         else:
#             print("Invalid password")
#
#     def set_password(self, password):
#         if len(password) > 10:
#             self.__password = password
#             print("Set to correct", self.password)
#         else:
#             print("Not allowed, weak password")
#
#
# pwd = Password("Hacker123")
# # pwd.get_password(True)
# pwd.set_password("pramod1")





