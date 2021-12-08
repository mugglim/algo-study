import time

# while loop
def twoPointerWithWhileLoop(arr, target):
    ans = -1
    l, r = 0, len(arr) -1

    while(l < r):
        total = arr[l] + arr[r]
        if total == target:
            ans = [arr[l], arr[r]]
            break
        if total < target: l += 1
        if total > target: r -= 1

    return ans

# for loop
def twoPointerWithForLoop(arr, target):
    ans = -1
    length = len(arr)
    r = 0

    for l in range(length):
        while r < length and arr[r] + arr[l] < target: r += 1
        if r == length: break
        if arr[r] + arr[l] >= target:
            if arr[r] + arr[l] == target: ans = [arr[l], arr[r]]
            break

    return ans


def getTime(cb, args):
    st = time.time()
    cb(*args)
    return time.time() - st


TARGET = int(1e7)
arr = [x for x in range(TARGET + 1)]

print(getTime(twoPointerWithWhileLoop, [arr,TARGET // 2])) # 1.517s
print(getTime(twoPointerWithForLoop, [arr,TARGET // 2])) # 0.96s
