shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    insertion_sort(prices)
    insertion_sort(coupons)
    result = 0
    for index in range(len(prices)):
        if index < len(coupons):
            result = result + prices[index] * (1 - coupons[index]/100)
        else:
            result = result + prices[index]
    return result


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] < array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return


print(get_max_discounted_price(shop_prices, user_coupons))