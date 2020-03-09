# 插值查找
def search_insert(arr, key):
    left, right = 0, len(arr) - 1
    while (left <= right):
        # 相等判断
        if arr[right] == arr[left]:
            if arr[left] == key:
                return left
            else:
                return -1
        mid = left + (key - arr[left]) // (arr[right] - arr[left]) * (right -
                                                                      left)
        # 选取下标判断
        if mid < left or mid > right:
            return -1
        if (arr[mid] == key):
            return mid
        if (arr[mid] > key):
            right = mid - 1
        if (arr[mid] < key):
            left = mid + 1
    return -1


if __name__ == '__main__':
    arr = [2, 2, 2, 2]
    key = 2
    index = search_insert(arr, key)
    if index == -1:
        print("%s不存在元素%s。" % (arr, key))
    else:
        print("%s位于%s下标为%s的位置。" % (key, arr, index))