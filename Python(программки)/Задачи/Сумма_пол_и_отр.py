b=0
c=0
while True:
    a=int(input())
    if a<0:
        b=b+a
    elif a>0:
        c=c+a
    else:
        break
print(b,c)
