arr=[int(x) for x in input().split()]
k=int(input())
lst=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        d=arr[i]+arr[j]
        if d==k:
            lst.append(arr[i])
            lst.append(arr[j])
            break
if len(lst)==0:
    print("No pairs found")
else:
    print(*lst)