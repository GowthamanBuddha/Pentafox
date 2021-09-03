import random
l=['Tamil','English','Maths','Science','Social']
day=['Monday','Tuesday','Wednesday','Thursday','Friday']
time=['9-10','10-11','11-12','1-2','2-3']
t=0
for i in time:
    if t==0:
        print("\t",end="   ")
    t=1
    print(i,end="   ")
print()
print(day[0],'\t',end="")
lr = random.sample(l, len(l))
print(*lr)
print(day[1],end=" ")
lr = random.sample(l, len(l))
print(*lr)
print(day[2],end=" ")
lr = random.sample(l, len(l))
print(*lr)
print(day[3],end=" ")
lr = random.sample(l, len(l))
print(*lr)
print(day[4],end="  ")
lr = random.sample(l, len(l))
print(*lr)