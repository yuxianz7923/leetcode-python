def maopao (list1):
    if len(list1) < 2:
        return list1
    for i in range (0, len(list1)):
        for j in range(i,len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1


list1 = [1,33,41,22,1,34,33,0]
print(maopao(list1))