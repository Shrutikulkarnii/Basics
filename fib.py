n= 50
a = 0
b = 1
c = 0
cnt = 0
while c < n:
    print(a, end =' , ')
    c = a + b
    a = b
    b = c
    cnt += 1
