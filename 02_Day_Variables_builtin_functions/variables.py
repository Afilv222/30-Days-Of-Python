
# Variables in Python

import math


first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print(len('Hello, World!'))
print(type(person_info))


# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


# Day 2: 30 Days of python programming

first_name = 'Afil'
last_name = 'Vidyasagar'
full_name = first_name + ' ' + last_name
country = 'Canada'
city = 'Calgary'
age = 25
year_born = 2000
is_married = 'Not yet'
is_true = True
is_light = False

today_weather,season,temperature = 'Sunny','Spring',10

num_one,num_two = 5,4

print(type(first_name))
print(f"First name length: {first_name} -> {len(first_name)}, last name length: {last_name} -> {len(last_name)}" )
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))    
print(type(year_born))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(today_weather))
print(type(season))
print(type(temperature))


total = num_one + num_two 
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**(num_two)
floor_division = math.floor(division)


print(total)
print(diff)
print(product)
print(division)

# how mod works is by taking the remainder of the numbers meaning, 4 % 5 is about 0.8 -> we floor the number meaning we round down 
# then we take 5 x 0 which gives us 0. We need substract to get the remainder 4 - 0 = 4 so our answer is 4.

# If we do 155 % 7 which is about 22.1428... then we take 22 and mutiple it by 7 which gives us 154, then we take 155 - 154 which is 1, the reminader is 1 

#Similar to when we do 6 % 2 which is 3 then we take 3 and multiple it by 2 which gives us 6, then we take 6 - 6 which is zero 


print(remainder)
print(exp)
print(floor_division)



# Calculating radius of circle 


radius = 0.3 

def calculate_area(radius):
    return math.pi * (radius)**2

area_of_circle = calculate_area(radius)

print(f'The area of a circle with radius 30: {area_of_circle}')

def calculate_circumference(radius):
    return 2 * math.pi * (radius)

circum_of_circle = calculate_circumference(radius)

print(f'The circumference of a circle with radius 30: {circum_of_circle}')

custom_radius = float(input("Enter in Radius: "))

print(f'The area of a circle with radius {custom_radius}: {calculate_area(custom_radius)}')




