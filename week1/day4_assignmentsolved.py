#1 Create three variables — your name, age, and height. Print them using an f-string in a single line like: - My name is ___, I am ___ years old and my height is ___ cm."
print("Que1: Create three variables — your name, age, and height. Print them using an f-string in a single line like: - My name is ___, I am ___ years old and my height is ___ cm.")
name= "Saurabh"
age= 28
height = 5.7
print(f"My name is {name}, I am {age} years old and my height is {height} cm.")

#2
print("\nQue2: Take a variable num_str = 25. - Convert it to an integer, multiply it by 2, and print both the type and value using an f-string.")
num_str= "25"
num_int= int(num_str)
result = num_int*2
print(f"Result for num_str is {result}, Type is {type(result)}")

#3
print("\nQue3: Write a program that takes two numbers and prints their sum, difference, product, quotient, and remainder using appropriate arithmetic operators.")
num1 = 50
num2 = 40
print (f"Sum of num1 and num2 is {num1+num2}")
print (f"Difference of num1 and num2 is {num1-num2}")
print(f"Product of num1 and num2 is {num1*num2}")
print(f"Quotient of num1 and num2 is {num1/num2}")
print(f"Remainder of num1 and num2 is {num1%num2}")

#4
print("\nQue4: Create a variable base = 3 and power = 4. Calculate 3⁴ using the exponential operator and print the result using an f-string.")
base = 3
power = 4
result = base**power
print(f"Result for base is {result}, Type is {type(result)}")

#5
print("\nQue5:  Start with x = 10. Use compound assignment operators (+=, -=, *=, /=, **=, %=, //= ) one by one and print the value of x after each operation.")
x = 10
x+=5
print(f"Result for x is {x}, Type is {type(x)}")

x -=5
print(f"Result for x is {x}, Type is {type(x)}")

x*=5
print(f"Result for x is {x}, Type is {type(x)}")

x/=5
print(f"Result for x is {x}, Type is {type(x)}")

x**=5
print(f"Result for x is {x}, Type is {type(x)}")

x%=5
print(f"Result for x is {x}, Type is {type(x)}")

x//=5
print(f"Result for x is {x}, Type is {type(x)}")