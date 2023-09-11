def maximumPower(s):
    # Write your code here
    n = len(s)
    count,maxcount,zerocount= 0,0,0
    for i in range(n):
        if s[i]=='0':
            count+=1
            zerocount+=1
        else:
            maxcount = max(maxcount,count)
            count=0
    
    maxcount = max(maxcount,count)
    if (zerocount==n):
        return -1
    
    k = 0
    l = n-1
    firstcount,lastcount=0,0

    while(s[k]=='0'):
        firstcount+=1
        k+=1
    while(s[l]=='0'):
        lastcount+=1
        l-=1

    maxcount = max(maxcount, firstcount+lastcount)

    return maxcount

if __name__ == '__main__':
    s = input()

    result = maximumPower(s)
    print(result)