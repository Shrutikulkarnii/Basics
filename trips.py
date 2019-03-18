def find_sum(p,size,sum):
  for i in range(0,size-2):
      for j in range(i+1,size-1):
          for k in range(j+1,size):
              if p[i]+p[j]+p[k] <= sum:
                  print ( p[i],p[j],p[k] )
p=input("Enter numbers with space- ").split(" ")
p=list(map(int,p))
sum=int(input("Enter the sum- "))
size=len(p)
find_sum(p,size,sum)
