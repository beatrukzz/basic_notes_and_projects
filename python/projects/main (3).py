# calc area of a circle
# 2pir^2
import math
radius = float(input("Enter the radius of the circle: "))
area = 2*math.pi*radius**2       # alternative: area = math.pi*pow(radius,2)
print(f"The area of the circle is {round(area,2)}")

# pathagoras theorem
a = float(input("Enter the length of side a of your triangle: "))
b = float(input("Enter the length of side b of your triangle: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"the length of side c is {round(c,2)}")


