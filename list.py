#list can contains a group of elements having different data type while array can have single data type elements
from _pyrepl.commands import delete
from linecache import updatecache

sample_list=["Vibhor",28,49,"M"]
print(sample_list)

#indexing of a list

sample_list=["Vibhor",20,"M","Noida"]
print(sample_list[1])
#slicing of a list

sample_list=["Vibhor",28,"M","Noida"]
print(sample_list[1:3:2])

#range in the list
#range(start,stop,step)

a=list(range(1,100,10))
print(a)

"""
#operations using list
1.) append # only add elements in the list at the end.
2.) update to update any item in the list
3.) delete
"""

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
a.append(15)
print(a)

a=["Vibhor",20,"M","Noida"]
print(a)#update
a[0]="Singhal"
print(a)

a=["Vibhor",28,"M","Noida"]
print(a)
del a[0]
print(a)