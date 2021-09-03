import random
let="Pentafox"
l=let[::-1]
a=l.lower()
m=random.sample(let,1)
d=''.join(map(str,m))
b=d.upper()
c=b+a
print(c)