"""
#create list using for loop and range
my_list=range(1,100,10)
list=list(my_list)
print(list)
for i in my_list:
    print(i)

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



# find out maximum and minimum number in the list

def value():
    lst=[]
    user=int(input("enter the number you want="))
    for i in range(user):
        add=int(input(f"enter the element {i}="))
        lst.append(add)
    print(lst)
    maximum=max(lst)
    print(f"The maximum is {maximum}")
    minimum=min(lst)
    print(f"The minimum is {minimum}")

value()

"""

#3.) Find the common element from two lists

def common():
     lst1=[1,2,3,4,5,6]
     lst2=[2,3,4,1,2,7,8]
     s1=set(lst1)
     s2=set(lst2)
     unique=s1.intersection(s2)
     print(unique)
common()