a=list(input())
b=list(input())
c=""
d=""
for i in range(len(a)):
    if a[i] not in b:
        c+=a[i]
for j in range(len(b)):
    if b[j] not in a:
        d+=b[j]

print(c+d)
