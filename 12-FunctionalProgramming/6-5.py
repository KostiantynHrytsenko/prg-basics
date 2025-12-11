arr = [i for i in range(1,21)]

print(list(filter(lambda x: x % 2 == 0 or x % 3 == 0, arr)))