def factorial(a):
    c = 1
    i = 1
    while i <= a:
        c *= i
        i += 1
    return c


num = int(input())
print(factorial(num))
