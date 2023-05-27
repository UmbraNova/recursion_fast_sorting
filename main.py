nice_list = [5, 8, 9, 4, 2, 9, 1, 8]


def separator(lst):
    smaller_nums, equal_nums, bigger_nums = [], [], []
    if lst:
        anchor = lst[len(lst)-1]
        for num in lst:
            if num < anchor:
                smaller_nums.append(num)
            elif num == anchor:
                equal_nums.append(num)
            else:
                bigger_nums.append(num)

    return smaller_nums, equal_nums, bigger_nums


def fast_sorting(lst, sorted=[]):
    small, equal, big = separator(lst)
    if small:
        fast_sorting(small, sorted)
    if equal:
        for num in equal:
            sorted.append(num)
    if big:
        fast_sorting(big, sorted)

    return sorted


print(fast_sorting(nice_list))
