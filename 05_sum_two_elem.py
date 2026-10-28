def sum_two_elem(arr):
    n = len(arr)
    gap = len(arr) // 2
    while (gap > 0):
        for cur in range(gap, n):
            m_gap = cur
            while (m_gap >= gap) and (arr[m_gap] < arr[m_gap - gap]):
                t = arr[m_gap]
                arr[m_gap] = arr[m_gap - gap]
                arr[m_gap - gap] = t
                m_gap -= gap
        gap = gap // 2
    return arr
