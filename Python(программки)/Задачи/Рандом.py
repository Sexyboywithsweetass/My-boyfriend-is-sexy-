a=0
N=int(input())
from random import randint
for i in range(0,N,1):
    x = randint(1,1000000000000000000000)
    a=a+x
print(a/N)
