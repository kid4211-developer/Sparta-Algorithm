shop_menus = ["가지", "오이", "만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "오", "만두"]


def is_available_to_order(menus, orders):
    shop_menus.sort()
    search_result = True
    for item in shop_orders:
        start_index = 0
        end_index = len(shop_menus) - 1
        while start_index <= end_index:
            check_index = (start_index + end_index) // 2
            if shop_menus[check_index] == item:
                search_result = True
                break
            elif shop_menus[check_index] < item:
                start_index = start_index + 1
            else:
                end_index = end_index - 1
            search_result = False
        if search_result is False:
            return search_result
    return search_result


result = is_available_to_order(shop_menus, shop_orders)
print(result)
