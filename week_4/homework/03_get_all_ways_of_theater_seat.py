seat_count = 9
vip_seat_array = [4, 7]

# 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    way_count = 1
    cur_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        way_count = way_count * fibo_dynamic_programming(fixed_seat_index - cur_index, memo)
        print("way_count :", way_count)
        cur_index = fixed_seat

    print("cur_index :", cur_index)
    last_way_count = fibo_dynamic_programming(total_count - cur_index, memo)
    result = way_count * last_way_count
    return result


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))