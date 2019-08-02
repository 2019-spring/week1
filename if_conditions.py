# if expression: # expression that returns only TRUE/FALSE
#     pass # python's "do nothing" statement, this line is executed only if expression is TRUE

# a = 3 # this statment is assigning value '2' to a variable 'a'
# if a == 2 : # a == 2 , means if the value of 'a' is equal to '2'
#     print(f"yes the value of a is: {a}") # this line executed only if the expression (a == 2) is TRUE
# else:
#     print(f"the value of a is not equal to 2, it is :{a}") # this line executed only if the expression (a == 2) is FALSE

# a = 3 # this statment is assigning value '2' to a variable 'a'
# # if a < 10 :  # 3 < 10 , this statement will return TRUE/FALSE   
# if a != 10 :  # 3 < 10 , this statement will return TRUE/FALSE   
#     print(f"yes the value of a is less than 10: {a}") 
# else:
#     print(f"the value of a is not less than 10 :{a}") 



# cars = [ "toyota", "lexus",  "bmw", "audi", "merc" ] # list of strings

# for car in cars:
#     if car == 'fiat':  # 
#         print("I love this car: "+ car.upper())
#     elif car == 'bmw':
#         print("I hate this car: " + car.upper())
#     elif car == 'lexus':
#         print("This car is expensive: "+car.title())
#     else: 
#         print(car.title())

# cars = [ "Toyota", "Lexus",  "BMW", "Audi", "Merc" ] # list of strings

# for car in cars:
#     if car != 'fiat' and car.lower() == 'bmw':
#         print("I hate this car: " + car.upper())
#     elif car != 'fiat' and car.lower()  == 'lexus':
#         print("This car is expensive: "+car.title())
#     elif car != 'fiat':  # 
#         print("I love this car: "+ car.upper())
#     else: 
#         print(car.title())

# age = int(input("Enter your age: ")) # change the value of this variable to test the conditions you have below

# if age < 21 :
#     print("Alcohol is not allowed")
# elif (age >=21) and (age < 25):  # range of age should be (21, 25) 
#     print("Alcohol is allowed but not more than one bottle")
# else: 
#     print("Drinking kills you, you know that right?")

# cars = [ "toyota", "lexus",  "bmw", "audi", "merc" ] # list of strings
# car = input("Enter your car: ")

# if car not in cars:
#     print("Sorry we dont have " + car.upper())
# else: 
#     print(f"Yes we have {car.title()} in our show room")


# USING MULTIPLE LISTS

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} topping to your pizza")
    else:
        print(f"Sorry we dont have {requested_topping} topping")