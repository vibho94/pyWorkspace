#basis necessity of the functions :- Write once and use if multiple times,reduces the line of code and function should be called in the program to get the output

"""
def function_name(param1,param2,.....):
    function statements

Basic example
def sum(a,b):#parameters
    c=a+b
    print("The sum  is ",c)

sum(2,3)#arguments
sum(50,30)


#------ Return function
#difference between return and print:- simply print output to the console while return returns the value that can be used later in the program

def mul(a,b):
    c=a*b
    return f"The multiplication is {c}"
d=mul(10,20)# to show the output in the console using return we need to store the function in the variable
print(d)





#Difference btw local variable and local variable

#local variables defined and used within the function only
#Global defined outside the function

def sum(a,b):
    a=10
    b=20
    c=a+b
    return (c)

d=sum(10,30)#in this case we have defined the value of variables outside return function but while calling the function it is returning inside values as the variables are defined locally
print(d)

a=100 #defined as global variable
print(a)



#Example :- User enter a number , we have to identify that the entered number is odd or even

def odd_even():
    number=int(input("Enter the number to get checked:"))
    if number%2==0:
        print("Even")
    else:
        print("Odd")
    return(number)
a=odd_even()
print(a)

"""

#example to draw a triangle/patter by entering the user input

def lines():
    number=int(input("Enter the number of lines for triangle:"))
    for i in range(1,number+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    return f"The triangle of {number} lines has been created"
a=lines()
print(a)




