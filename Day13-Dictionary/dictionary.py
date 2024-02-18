# Dictionary
# Key and Value pair
# A dictionary is an unordered collection of data


# d={}         # empty dictionary
# print(d)
# print(type(d))
#
# d1=dict()     # empty dictionary
# print(d1)
# print(type(d1))


# phone_book={"pawan":9960374334,"basant":9897647996,"kajal":9999999999,"annu":8888888888}
# print(phone_book)
# print(len(phone_book))
#
# emp_code={101:"mamta",102:"aayushi",103:"vishal",104:"riya"}
# print(emp_code)
# print(len(emp_code))

# print(phone_book["basant"])
# print(emp_code[102])

# Iterate dictionary value using for loop

# for i in phone_book:      # print all key using for loop
#     print(i)

# for i in phone_book:      # print all value using for loop
#     print(phone_book[i])

#-------------------------------------------------------------------
# Dictionary create also this type

# phone_book2 = dict(Batman=123, Cersei=342, GB=323)
# print(phone_book2)

# print(phone_book2["GB"])
# print(phone_book2.get("GB"))     # Dictionary method
# print(phone_book2.keys())
# print(phone_book2.values())

# del phone_book2["Batman"]   # delete 1 item from dictionary
# print(phone_book2)

# phone_book2.clear()           # clear dictionary
# print(phone_book2)

# print(phone_book2.pop("Batman"))      # remove item from list
# print(phone_book2)





# for i in phone_book2.values():
#     print(i)
#
# for x in phone_book2.keys():
#     print(x)
#
# for y in phone_book2.items():
#     print(y)



# Automation Tester - Mobile, API and Web Automation

# my_dict = {'b': 2, 'a': 1, 'c': 3}
# for k,v in my_dict.items():
#     if k == 'b':
#         print("'b is found!")
#
# op = 'b' in my_dict
# print(op)

#--------------------------------------------------------------------

# api_response = {
#     "first_name": "Pawan",
#     "age": 28,
#     "last_name": "Pandit",
#     "email": "pawanpandit35@gmail.com",
#     "password": "Pawan123",
#     "commission": 10
# }
#
# print(api_response)
# print(type(api_response))
# print(api_response["email"])
# print(api_response.values())
# print(api_response.keys())
# print(api_response.get("password"))

# api_response["password"]="Pawan@123"     # password update
# print(api_response)


#---------------------------------------------------------------------------


# d={}
# key=input("enter key of dictionary:")
# value=input("enter value of dictionary")
# d[key]=value
# print(d)



















