# Define the list of the phone numbers

phone = {
    "Vibhor"  : 999999,
    "Shubham" : 88888,
    "Agam"    : 77777,
    "Vineet"  : 66666
}

#greet

print("Welcome to my phonebook :")
print("Vibhor :999999\nShubham  : 88888\nAgam  : 77777\nVineet : 66666")


Actions = {"Create","Read","Update","Delete"}

option_1 = input("Enter your option (Create/Read/Delete/Update): ")
if option_1 == "Read":
    name_1=input("Enter your name : ")
    if name_1 in phone:
        print(f'Your name is {name_1} and number is {phone[name_1]}')
    else:
        print(f"Name {name_1} is not in the phonebook")

elif option_1 == "Create":
    name_1 = input("Enter the name to be created: ")
    number_1 = input("Enter the phone number: ")
    if name_1 in phone:
        print(f"Duplicate name {name_1} is not allowed")
    else:
        phone[name_1] = number_1
        print(f"Name {name_1} has been added to the phonebook")


elif option_1=="Update":
    name_1 = input("Enter the contact name to be updated: ")
    if name_1 in phone:
        number_1 = input("Enter the new number: ")
        phone[name_1]=number_1
        print(f"Name {name_1} has been updated with the new number")
    else:
        print(f"Name {name_1} does not exist in the phonebook")

elif option_1 == "Delete":
    name_1 = input("Enter the name to be deleted: ")
    if name_1 in phone:
        del phone[name_1]
        print(f"Name {name_1} has been deleted from the phonebook")
    else:
        print(f"Name {name_1} does not exist in the phonebook")



else:
    print("Please enter a valid option")




