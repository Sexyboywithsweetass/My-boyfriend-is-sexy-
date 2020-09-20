a_1 = int(input("Push first element: "))
d = int(input("Push difference: "))
n = int(input("Push quantity: "))

list = [a_1 + (i - 1) * d for i in range(1, n + 1)]

print(list)
