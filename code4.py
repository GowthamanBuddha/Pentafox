s=input()
i = 0
while( i < len(s) - 1) :
    count = 1
    while s[i] == s[i + 1] :
        i += 1
        count += 1
        if i + 1 == len(s):
            break
    if(count>1):
        print(str(s[i]),end="")
        print(str(count),end="")
    else:
        print(str(s[i]),end="")
            
    i += 1