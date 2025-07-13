"""
For loop 3 fundamentals

1.) Start
2.) Stop
3.) Step

for i in range (start,stop,step):
   statements
   include and exclude
"""
#for i in range (1,10,2): # 1 is included and 10 is excluded , 2 is the incremented(step) value
 #   print(i)

# 2 number list with start and end number as input
"""
m= int(input("Enter the start number: "))
n= int(input("Enter the end number: "))
z=n+1 # since for loop excludes the last number , hence we have to add one number

for i in range(m,z,1):
    print(i)
    
"""

# 3. print reverse list with 2 numbers as input

m=int(input("Enter the start number: "))
n=int(input("Enter the end number: "))
z=n+1
if m<n:
    for i in range(m,z,1):
        print(n)
        n=n-1
else:
    print("The  start number should be less than the end number")
    



#4.) 1 to 100 %3

"""

m=int(input("Enter the start number: "))
n=int(input("Enter the end number: "))
div=int(input("Enter the number to divide by: "))

print(f'number divide by {div} from {m} to {n}')
for  i in range(m,n+1):
    if i%div==0:
        print(i)

"""