
def two_sum(arr: list[int], target: int) -> list[int]:
    map = {}

    for i, curr_n in enumerate(arr):
        looked_num = target - curr_n
        if looked_num in map.keys():
            return [i, map[looked_num]]
        map[curr_n] = i

    # res = []
    # found_sum = False
    #
    # for i in range(len(arr)):
    #     curr_el = arr[i]
    #
    #     for next_i in range(i + 1, len(arr)):
    #         if curr_el + arr[next_i] == target:
    #             res.extend([i, next_i])
    #             found_sum = True
    #             break
    #
    #     if found_sum:
    #         break


nums = [0, 4, 3, 0]
target = 0

print(two_sum(nums, target))
