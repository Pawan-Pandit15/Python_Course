# # # # Match Case
# # # # Switch
# # # numbers = int(input("Enter a Number 1-6:\n"))
# # # match numbers: #BREAK IS NOT NEEDED in case of Match and CASE
# # #     case 1:
# # #         print("You have entered 1")
# # #     case 2:
# # #         print("You have entered 2")
# # #     case 3:
# # #         print("You have entered 3")
# # #     case 4:
# # #         print("You have entered 4")
# # #     case 5:
# # #         print("You have entered 5")
# # #     case 6:
# # #         print("You have entered 6")
# # #     case _:
# # #         print("No idea")
# #
# #
# #
# #
# # x = int(input("Enter the value of x: "))
# # # x is the variable to match
# # match x:
# #     # if x is 0
# #     case 0:
# #         print("x is zero")
# #     # case with if-condition
# #     case 4:
# #         print("case is 4")
# #
# #     case _ if x!=90:
# #         print(x, "is not 90")
# #     case _ if x!=80:
# #         print(x, "is not 80")
# #     case _:
# #         print(x)
#
#
#
#
# browser = str(input("Enter the browser name:\n"))
# browser = browser.lower()
# match browser:
#     case "chrome":
#         print("Chrome code executed!")
#     case "firefox":
#         print("Firefox  code executed!")
#     case "google":
#         print("Google browser executed!")
#     case "fb":
#         print("you are enter facebook")
#     case "insta":
#         print("you are enter instagram")
#     case _:
#         print("No browser Found!")
#
#

#

# browser = str(input("Enter the browser name:\n"))
# browser = browser.lower()
# match browser:
#     case "chrome":
#         print("Chrome code executed!")
#     case "firefox":
#         print("Firefox code executed!")
#     case "google":
#         print("Google browser executed!")
#     case browser if browser == "fb":
#         print("you are enter facebook")
#     case browser if browser == "insta":
#         print("you are enter instagram")
#     case _:
#         print("No browser Found!")