def anagram_array(arr):
    Hash = {}
    for i in arr:
        m = ''.join(sorted(list(set(i))))
        if m in Hash:
            Hash[m].extend([i])
        else:
            Hash[m] = [i]
    res = []
    for i in Hash:
        res.append([Hash[i]])
    return res
