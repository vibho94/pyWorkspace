"""
1.) Print the below pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *


for i in range (1,6):
    for j in range (1,6):#1 iteration complete
        print("*",end=" ")
    print()



2.) Print the below pattern:-
*
* *
* * *
* * * *
* * * * *


r=5 # decide the number of rows
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

3.) Print the below pattern:-

* * * * *
* * * *
* * *
* *
*



r=5
for i in range(r,0,-1): #(5,0,-1)
    for j in range(i):
        print("*",end=" ")
    print()


4. print the below patter :-
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


n=5
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end=" ")
    print()

5.) Print the below pattern :-
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


from qrcode.util import pattern_position

n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

6.) Print the below pattern

        *
      * * *
    * * * * *
   * * * * * *
 * * * * * * * * *



n=9

for i in range(1,n+1,2):#(1,9)
    for k in range(n,i,-2):
        print(" ",end=" ")
    for j in range(1,i+1):#(1,2)
        print( "*",end=" ")
    print()


7.) Print the below pattern :-

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""

n=9
for i in range(1,n+1,2):#(1,9)
    for j in range(n,i,-2):#(9,1)
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()


for i in range(n-2,0,-2):#(7,1)
     for j in range(n-i,0,-2):#(2,1)
         print(" ",end=" ")
     for k in range(i):#(7,1)
        print("*",end=" ")
     print()