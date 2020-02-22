def quick_sort(alist, start, end):
    if start >= end:
        return
    mid = alist[start]  # 设定起始的基准元素
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        print(alist)
        print(mid, high, low, mid)
        alist[low] = alist[high]
        print(alist)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while low < high and alist[low] < mid:
            low += 1
        print(alist)
        print(mid, high, low)
        alist[high] = alist[low]
        print(alist)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    alist[low] = mid  # 将基准元素放到该位置,
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)

if __name__ == '__main__':
    alist = [9, 55, 7, 0, 108, 2, 11]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
