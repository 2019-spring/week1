# Syntax:
# create a list or use existing list
# for target_list in expression_list:
#     pass

# cars = [ ["toyota", "lexus"],  ["bmw", "audi"], ["merc"] ] # list of lists
# # cars = [ "toyota", "lexus",  "bmw", "audi", "merc" ] # list of strings

# for car in cars:
#     print(car) # logic for each object in the cars list
#     # print(car + " is a nice car")
#     for target in car:
#         # pass - do nothing 
#         print(target) # logic for each sub object in the object of the cars list

# print("thats nice collection")

# # students = ['nurbek', 'farzona', 'jamoliddin']
# # for var in students:
# #     print(var + ", please submit your homework on time.")

# # loops with numbers
# # for number in range(2, 6):
# #     print(number, number**2) # ** means square of the number

# # list() - creating a list from range() function result
# numbers_list = list(range(3, 9)) 
# print(numbers_list)

# for num in numbers_list:
#     print(num, num+10)
# # for number in range(2, 10, 2):
# #     print(number)

# # create list of squares from the existing list of numbers
# numbers_list = list(range(3, 9)) 
# squares_list = []

# print(squares_list)

# number_list = list(range(3,9)) # range >> 3, 4, 5, 6, 7,8 : list(range) >> [3, 4, 5, 6, 7, 8]
# square_list =[]
# for number in number_list:
#     print(square_list)
#     square_list.append(number**2)

# print(square_list)

# print(max(square_list))
# print(min(square_list))
# print(sum(square_list))

# # square_list = [number**2 for number in number_list]
# print(square_list)

# # exercise 4-3
# for num in range(1, 21):
#     print(num)
# # exercise 4-4
# for num in range(1, 1000001):
#     print(num)
print("############## 07/25/2019 ############")
# 
new_cars = [ "toyota", "lexus",  "bmw", "audi", "merc" ] # list of strings

print(new_cars[:3]) # starting from the begining of the list , include index 0, 1, 2
print(new_cars[1:4]) # 3 objects will be printed , this range include index 1, 2, 3
print(new_cars[2:]) # starting from the 2nd index object until the end of the list , includes indexes 2, 3, 4
print(new_cars[-2:])
