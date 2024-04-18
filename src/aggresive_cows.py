

def can_place_cow(stalls, cows, dist):
    n = len(stalls)
    cound_cows = 1
    last = stalls[0]
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cound_cows += 1
            last = stalls[i]
        if  cound_cows >= cows:
            return True
    return False

def aggresive_cows(stalls, cows):
    n = len(stalls)
    stalls.sort()
    low = 1
    high = stalls[n-1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if can_place_cow(stalls, cows, mid):
            low = mid + 1
        else:
            high = mid - 1
    return high

