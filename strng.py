"""
#string is a collection of words or alphabets or other characters
s1="Vibhor" #valid
s2='Singhal' #valid
s3="""
#Vibhor
#Singhal
""" #multiline stirng, we can use single comma or double comma
print(s1,s2,s3)

# My name is 'Vibhor'

string= "My name is 'Vibhor'"
print(string)

string='Vibhor'
print(len(string))

#index in string
string='Vibhor'
print(string[4])
print(string[-1]) #when the length of the string in unknown ,-1 indicates that the indexing starts from the end

string='I love python'
l=len(string)

for i in string:
    print(i,end=" ")
    #print()
print()


for i in string[: :-1]:#slicing in string [start :stop :step]
    print(i,end=" ")

#slicing the string
start=0 :- by default value
stop=n-1 :- by default value
step=1 :- by default value


string="I love python"
#print(string[2:5:0]) can not be zero
print(string[3:5:1])

"""

#repeat the string
"""
string_name*n


string='python'
print('python'*5)
print(string[0]*5)# to print a particular character in the string
sliced=string[2:5:2]# to print some characters in the string # start from 2 and end at 5-1=4 while taking every 2nd character
print(sliced*5)
"""
#concatenation operator

# Membership operator
"""
Type of membership operator
in
not in


main_str=input("enter the main string:")
sub_str=input("enter the sub string:")
if sub_str in main_str:
    print(f"{sub_str} is present in the main string")
else:
    print(f"{sub_str} is not present in the main string")


#comparison of two strings

name='Vibhor Python'
if name=='Vibhor Python':
    print(True)
else:
    print(False)

# if we have left or right space with the string,we can use strip method,strip() to remove the leading nd trailing spaces , like :-

name='  Vibhor Python '
if name.strip()=='Vibhor Python':#lstrip to remove left space /rstrip to remove right space
    print(True)
else:
    print(False)


"""

#counting of the character in the string
main_str='Noida is near Delhi'
#total=main_str.count('i')
total=main_str.count('i',2,10)
print(total)



