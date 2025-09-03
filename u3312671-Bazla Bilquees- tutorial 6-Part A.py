# A simple function (we used it so that we cant rewrite again) 
def greet(name): #function
    # Return a friendly greeting:
    return f"Hello, {name}!"

# Using the function
message = greet("Aisha")
print(message)  # Hello, Aisha!

def area_of_rectangle(width, height):
    return width * height
print(area_of_rectangle(3, 5))   # 15

def power(base, exponent=2):
    return base ** exponent
print(power(5))          # 25 (uses default exponent=2)
print(power(2, exponent=3))  # 8 (keyword argument)

PI = 3.14159  # global variable (AT the top of the document)
def circle_area(r):
    "Compute area of a circle of radius r."
    return PI * (r ** 2)

print(circle_area(2))  # 12.56...
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def is_even(n):
    return n % 2 == 0

def triangle_area(b, h=1):
    return 0.5 * b * h
message = greet("Bazla")
print(message) #Hi, Bazla

def main():
    print(message)  # Hello, Aisha!
    print(area_of_rectangle(3, 5))   # 15
    print(power(5))          # 25 (uses default exponent=2)
    print(power(2, exponent=3))  # 8 (keyword argument)
    print(circle_area(2))  # 12.56...
    
    
