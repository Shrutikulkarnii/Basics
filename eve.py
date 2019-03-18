def check(p):
    m=0
    n=0
    for i in p:
        if i%2 == 0:
            m += 1
        else :
            n += 1
    return m,n
p=input("Enter numbers with space- ").split(" ")
p=list(map(int,p))
(m,n)=check(p)
print("Nmber of even numers are: " ,m , "Number of odd numbers are: ", n)
