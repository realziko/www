def min_platforms(arr, dep):
    n = len(arr)
    arr.sort()
    dep.sort()

    platformn = 1
    res = 1
    i = 1
    j = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platformn += 1
            i += 1
            if platformn > res:
                res = platformn
        else:
            platformn -= 1
            j += 1

    return res

n = 6
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arr, dep))
