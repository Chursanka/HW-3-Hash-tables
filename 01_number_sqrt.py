def find_sqrt(target):
    mini = 0
    maxi = target
    while (mini <= maxi):
        mid = (mini + maxi) // 2
        if (mid ** 2 > target):
            maxi = mid - 1
            continue
        elif (mid ** 2 < target):
            mini = mid + 1
            continue
        return mid
    return maxi
# На каждом шаге мы отсекаем половину чисел => на k-1-ом шаге у нас останется два числа, и на k-ом останется одно - наш ответ => Сложность логарифмическая
