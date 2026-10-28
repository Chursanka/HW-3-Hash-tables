def find_sqrt(target):
    mini = 0
    maxi = target
    while (mini < maxi):
        mid = (mini + maxi) * 0.5
        if (mid ** 2 > target):
            maxi = mid - 1
            continue
        elif (mid ** 2 < target):
            mini = mid + 1
            continue
        else:
            return mid
    return -1
