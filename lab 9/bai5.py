def permutation(arr):
    if len(arr) == 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutation(remaining):
            result.append([current] + p)
    return result
n = int(input("Nhập n: "))
arr = list(range(1, n + 1))
print(permutation(arr))