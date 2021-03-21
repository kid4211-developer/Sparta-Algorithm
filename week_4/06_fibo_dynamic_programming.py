input = 100

memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n not in fibo_memo:
        result = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
        fibo_memo[n] = result
        return result
    else:
        return fibo_memo[n]


print(fibo_dynamic_programming(input, memo))