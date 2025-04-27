
def find_max_num(arr):
    max_idx = 0

    for i in range(1, len(arr)):
        if arr[max_idx] < arr[i]:
            max_idx = i

    return arr[max_idx]

arr = [2, 4, 18, 6]
print(find_max_num(arr))