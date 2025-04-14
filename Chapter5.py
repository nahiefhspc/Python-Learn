import math
x = 9.3
#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
result = math.floor(x)
print(result)



#Circumference of circle
import math
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"Op {round(circumference, 2)}")


#Area of circle
import math

radius = float(input("Enter the radius : "))

area = math.pi * pow(radius, 2)

print(f" Area - {round(area, 2)}")


#Pythagous
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print (f" Side C = {c}")



