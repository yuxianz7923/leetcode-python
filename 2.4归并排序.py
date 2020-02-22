
def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        # print("lefthalf: ", lefthalf)
        righthalf = alist[mid:]
        # print("righthalf: ", righthalf)
        mergesort(righthalf)
        mergesort(lefthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                # print(lefthalf[i], righthalf[i], len(lefthalf), len(righthalf))
                # print("lefthalf: ", lefthalf)
                # print("righthalf: ", righthalf)
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k = k + 1
            print(alist)
            print("-------------")
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
