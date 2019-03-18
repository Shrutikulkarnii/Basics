def swap(a,b):
    temp=0
    temp=a
    a=b
    b=temp
def check(x):
    x.isalpha()

def rev(string):
    p=list(string)
    l=0
    r=len(p)
    while l < r:
        if not check(p[l]):
            l+=1
        elif not check(p[r]):
            r-=1
        else:
            swap(p(l),p(r))
string=input("Enter a string: ")
rev(string)
print(string)
