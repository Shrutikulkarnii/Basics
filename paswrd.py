import re
p= input("enter password: ")
c=True
while c:
    if not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif (len(p)<6 or len(p)>16):
                break
    else:
        print("password is valid")
        c=False
        break

if c:
    print("not a valid password")
