def maximumStones(arr):
    # Write your code here
    oddStone = []
    evenStone = []
    for index,val in enumerate(arr):
        if index%2==0:
            oddStone.append(val)
        else:
            evenStone.append(val)
    
    if sum(oddStone)==sum(evenStone):
        return sum(oddStone) + sum(evenStone)
    elif sum(oddStone)<sum(evenStone):
        return 2*sum(oddStone)
    else:
        return 2*sum(evenStone)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = maximumStones(arr)
    print(result)
