# Write a function called area_circumference_generator that takes a radius of a circle as a function parameter and calculates its circumference and area. Then returns these two results as a tuple and prints the results using tuple unpacking in the function call accorrding to the given format. [Must use tuple packing & unpacking]
# Example1: 
# Function Call: area_circumference_generator(1)
# Output:
# (3.141592653589793, 6.283185307179586)
# Area of the circle is 3.141592653589793 and circumference is 6.283185307179586
# Example2: 
# Function Call: area_circumference_generator(1.5)
# Output:
# (7.0685834705770345, 9.42477796076938)
# Area of the circle is 7.0685834705770345 and circumference is 9.42477796076938
# Example3: 
# Function Call: area_circumference_generator(2.5)
# Output:
# (19.634954084936208, 15.707963267948966)
# Area of the circle is 19.634954084936208 and circumference is 15.707963267948966
def area_circumference_generator(x):
    z = tuple()
    import math
    a = math.pi* x**2
    c = 2*math.pi*x
    z = a, c
    print(z)
    p, q = z
    print(f"Area of the circle is {p} and circumference is {q}")
area_circumference_generator(2.5)