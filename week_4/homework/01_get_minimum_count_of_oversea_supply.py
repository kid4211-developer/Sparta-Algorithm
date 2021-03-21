import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# key point !
# 1. stock이 충당 되어야할 total stock을 넘는다면 더이상 추가 공급은 필요없음
# 2. date가 현재 stock을 넘어 선다면 더이상 체크할 필요가 없음(왜냐하면 그 날짜까지 공장이 버틸수가 없다는 의미이므로)
# 3. date별 supply stock 탐색이 끝나면 현재 stock에 공급량 만큼 더해준다.
def get_minimum_count_of_overseas_supply(dates, supplies):
    stock = ramen_stock
    min_result = 0
    cur_data_index = 0
    max_heap = []
    while stock < supply_recover_k:
        for date_index in range(cur_data_index, len(dates)):
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                cur_data_index = date_index
                break
        min_result += 1
        stock = stock + -heapq.heappop(max_heap)
    return min_result


print(get_minimum_count_of_overseas_supply(supply_dates, supply_supplies))