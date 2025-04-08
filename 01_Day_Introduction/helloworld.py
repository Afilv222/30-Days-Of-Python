# Introduction
# Day 1 - 30DaysOfPython Challenge
import math

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

# This is finding  Euclidian distance between tuples 
# (x-axis,y-axis)
point1 = (2,3)
point2 = (10,8)

d1= math.dist(point1,point2)
d2 = math.sqrt( (point2[0] - point1[0] ) ** 2 + (point2[1]  - point1[1] ) ** 2 )



print(d1)
print(d2)
