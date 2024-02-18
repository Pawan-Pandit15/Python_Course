# List
# List - Collection of Items( Duplicate is allowed)
# List is mutable


# my_list=[1,2,3,9,4,5,5,6]
# print(type(my_list),my_list)
# my_list[1] = 20      # changing element
# print(my_list[2])
# print(len(my_list))
# my_list.append(8)
# print(my_list)
# print(my_list, my_list.count(5))
# print(my_list, my_list.pop(4))
# print(my_list, my_list.sort())
# print(my_list, my_list.remove(9))
# print(my_list, my_list.reverse())


# l2=[1,4,5,"pawan",True,2.3,"pandit"]
# print(l2)
# print(type(l2))
# print(l2[3])
# tu=tuple(l2)    # conver list to tuple
# print(tu)
# print(type(tu))

# for i in my_list:
#     print(i)
#     if i==4:
#         break
# print("break statement executed")


# l1=[1,3,5,6,7,9]

# for i in l1:
#     if i==5:
#         print("continue statement executed")
#         continue
#     print(i)


# for i in l1:
#     print(i)
#     if i==5:
#         pass





# Map()

# def sq_of_number(num):
#     return num ** 2
#
#
# # result = sq_of_number(10)
# # print(result)
#
# numbers = [1, 2, 3, 4, 5]
#
# # Map()
# # 1. Takes Each item from the list
# # 2. execute the function on it.
# # 3. Return same number of elements ( list)
#
# sq_numbers = list(map(sq_of_number,numbers))
# # 1,4,9, 16,25
# print(sq_numbers)
