a=list(map(int,input().split(',')))
b=''
c=64
for i in a:
    d=c+i
    b+=chr(d)
print(b)