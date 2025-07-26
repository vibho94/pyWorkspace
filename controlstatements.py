#control statements are the statement which control or change the flow of execution ,normal we write the program in sequential flow
"""
pi=3.1415926
radius =int(input("Enter the radius of the circle: "))
Area_circle=pi*radius*radius
print(f"The area of the circle is: {Area_circle}")

"""
#if number is even or not

number=int(input("Enter the number: "))
if number % 2==0:
    print("The number is even")
elif number % 2!=0 and number >=1:
       print("The number is odd")
else:
    print("Please enter a valid number")