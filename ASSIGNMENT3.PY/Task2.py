import math

num = float(input("Enter a positive number: "))


angle = float(input("Enter angle in degrees: "))

print("\n---- RESULTS ----")

if num >= 0:
    print("Square Root:", math.sqrt(num))
else:
    print("Square root not defined for negative numbers")

if num > 0:
    print("Natural Log (base e):", math.log(num))
    print("Log base 10:", math.log10(num))
else:
    print("Logarithm not defined for zero or negative numbers")


radian = math.radians(angle)
print("Sine value:", math.sin(radian))
