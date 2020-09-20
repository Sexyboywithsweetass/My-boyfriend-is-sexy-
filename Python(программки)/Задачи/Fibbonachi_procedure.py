from random import randint


def fib(num):
    per = a = 0
    i = sum = 1
    print("0 element:", sum)
    while i <= num:
        a = sum
        sum += per
        per = a
        print(i, "element:", sum)
        i += 1


low_range = 1
high_range = 10
number = randint(low_range, high_range)
print(number)
fib(number)
