arr = [1, 2, 3, 4, 5]

print(arr)

for i in arr:
    arr[i-1] = arr[i - 1] - 1

print(arr)