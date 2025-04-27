
def recursive_sum(arr, i=0):

    if i == len(arr) - 1:
        return arr[i]

    return arr[i] + recursive_sum(arr, i+1)

arr =[5, 10, 74, 3, 8]
print(recursive_sum(arr))