# if = Do some code If some condition is True
 #         Else do something else
 
age = int(input("Enter your age :"))

if age >= 100:
    print("You are too much")
elif age>= 18:
    print("You are now signup up!")
elif age < 0:
    print("You haven't born born yet!")
else:
         print("You must be 18+ to sign up")

response = input("what you like food (Y/N)")

if response == "Y":
    print(" Have some food")
else:
    print("No food for you")


#Exercises
name = input("Enter your name: ")

if name == " ":
    print(" You did not type in your name !")

else:
    print(f"Hello {name}")


for_sale = True

if for_sale:
    print("This item for sale!")
else:
        print("This item is NOT for sale")



# Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input(" Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
    
else:
    print(f"{operator} is not valid")


#Python weight converter

weight = float(input("Enter your weight: "))
unit = input(" Kilogram or Pounds? (K or L): ")

if unit == "K":
  weight = weight * 2.205
  unit = "Libs"
print(f"Your weight is: {weight} {unit}")
  
elif unit == "L":
  weight = weight / 2.205
  unit = "Kgs"
print(f"Your weight is: {weight} {unit}")

else:
  print(f" {unit} is not valid")



#Exercise
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
  temp = round((9 * temp / 5 + 32, 1)
  print(f"The temperature in Fahrenhit is: {temp}°F")
               
elif unit == "F":
  temp = round((temp - 32) * 5 / 9, 1)
  print(f"The temperature in Celcius is: {temp}°C")

else:
  print(f"{unit} is an invalid unit")
