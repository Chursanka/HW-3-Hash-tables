def easy_task(n, x, y):
    mini = 0
    maxi = (n - 1) * max(x, y)
    while (mini + 1 < maxi):
        mid = (mini + maxi) // 2
        cnt = mid//x + mid//y
        if ( cnt < n - 1):
            mini = mid
            continue
        elif (cnt > n - 1):
            maxi = mid
            continue
        return mid + min(x, y)
    return maxi + min(x, y)
# времени будет достаточно, если n-1 лист будут напечатаны за mid времени, тогда ответом будет mid плюс время печати первого листа (минимальное из двух принтеров)
