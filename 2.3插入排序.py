def charu (list3):
    if len(list3) < 2:
        return print(list3)
    for i in range (1, len(list3)):
        current_data = list3[i]
        pre_index = i-1
        while list3[i] < list3[pre_index]:
            list3[i], list3[pre_index] = list3[pre_index], list3[i]
            i -= 1
            pre_index -= 1
    return print(list3)

list3 = [1,43,55,67,6,888]
charu(list3)