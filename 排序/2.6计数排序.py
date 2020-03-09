def CountingSort(arr):
    if not isinstance(arr,(list)):
        raise TypeError('error para type')
    maxNum=max(arr)
    minNum=min(arr)
    length=maxNum-minNum+1
    tempArr=[0 for i in range(length)]
    resArr=list(range(len(arr)))
    for num in arr:
        tempArr[num-minNum]+=1
    print(tempArr)
    for j in range(1,length):
        tempArr[j]=tempArr[j]+tempArr[j-1]
    print(tempArr)
    print(resArr)
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],i)
        resArr[tempArr[arr[i]-minNum]-1]=arr[i]
        tempArr[arr[i]-minNum]-=1
    return resArr
if __name__=='__main__':
    arr=[12,25,26,13,14,25,12,17,18,14]
    print(CountingSort(arr))


