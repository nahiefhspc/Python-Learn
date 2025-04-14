# input() = A function that promots the user to enter data Returns the entered data as a string

name = input("What is your name?:")
age = int(input("How old are you"))

#age = int(age)
age = age + 1

print(f"Hello {name}")
print(f"Age {age}")



# Exercise 1 Recatangle Area Calc

length = int(input("Enter the length: "))
width = int(input("Enter the Width: "))
area = length * width
#Try - Float,Int

print(area)





# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy? ")
price = float(input(" What is Price ? "))
quantity = int(input(" How many would you like?: "))
total = price * quantity

print(f" You Have bought {quantity} × {item}/s")
print(f"Your total is : {total}")




