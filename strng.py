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
"""

string='python'

