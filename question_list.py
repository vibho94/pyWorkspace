"""
#create list using for loop and range
my_list=range(1,100,10)
list=list(my_list)
print(list)
for i in my_list:
    print(i)
"""
# create list as per user input and display its sum


def sum():
    lst=[]
    user=int(input("enter the number you want="))
    for i in range(user):
        choice=int(input(f"enter your element {i}="))
        lst.append(choice)

    total=0
    #lst=[1,2,3]
    for i in range(len(lst)):
        total=total+lst[i] #i=0 ,lst[0]
        #o=o+1
        #1=1+2
    return f"The total is {total}"
s=sum()
print(s)

