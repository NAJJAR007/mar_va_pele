while 1:
    try:
        a = int(input("enter your list for check : "))
        break
    except ValueError:
        print("try again")

check_list = []

while 1:
    if type(a) == int:
        check_list.append(a)
        a = input("enter your list for check : ")
        if a.isdigit():
            a = int(a)
        else:
            pass
    else:
        break

x = int(input("inter a check value : "))

is_group_member = True

for a in check_list:
    if x == a :
        is_group_member = True
        break
    else :
        is_group_member = False

print(check_list)
print(is_group_member)