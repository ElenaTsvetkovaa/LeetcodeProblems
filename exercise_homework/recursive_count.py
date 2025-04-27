

def count(arr, i=0):
    if i == len(arr):
        return 0
    return 1 + count(arr, i + 1)


arr = [2, 4, 6, 8]
print(count(arr))