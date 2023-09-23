

def bin_search(arr, num, left=0, right=None):
    if (right == None):
        right = len(arr) - 1
    midle = int((left + right) / 2)
    if (arr[midle] == num):
            return midle
    if (left < right):
        if (arr[midle] > num):
            return bin_search(arr, num, left, midle)
        if (arr[midle] < num):
            return bin_search(arr, num, midle + 1, right)
    return None


a = [1, 2, 3, 4, 6, 7, 9]

print(bin_search(a, 1))
