input = 100

global count
count = 0


def fibo_recursion(n):
    global count
    if n == 1 or n == 2:
        count += 1
        print(count)
        return 1
    count += 1
    print(count)
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))