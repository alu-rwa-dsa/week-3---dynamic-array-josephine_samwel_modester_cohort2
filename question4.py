# Authors: Samwel Maisiba, Modester Mwangi, Josephine Uwizeye

# Build an a list (associative list) which has the following methods
# a. add(key,value)
# b. remove(key)
# c. modify(key,newvalue)
# d. lookup(key)

dict1 = dict()
dict1["Name"] = "John"
dict1["Age"] = 23
dict1["School"] = "ALU"
dict1["Country"] = "Rwanda"
dict1["Major"] = "CS"
print(dict1)


def add():
    dict1[key] = value
    print(f"{dict1}\n")


def remove():
    dict1.pop(rmv.capitalize())
    print(f"{dict1}\n")


def modify():
    for k in dict1:
        if k.capitalize() == key.capitalize():
            dict1[k] = new_value
    print(f"{dict1}\n")


def lookup():
    for k in dict1:
        if k.capitalize() in search.capitalize():
            return True

    return False


ans = 0
while ans < 4:
    ans += 1
    action = int(input("Choose action\n1 ADD\n2 REMOVE\n3 MODIFY\n4 LOOK UP\n>>> "))
    if action == 1:
        key = input("Enter 'Key' to add: ")
        value = input("Enter 'Value' to add: ")
        add()

    elif action == 2:
        print(f"This is the dictionary {dict1}")
        rmv = input("Enter key of the value to remove: ")
        remove()

    elif action == 3:
        key = input("Enter 'Key' to modify: ")
        new_value = input("Enter 'Value' to modify: ")
        modify()

    elif action == 4:
        search = input("Enter key to search: ")
        print(f"{lookup()}\n")

