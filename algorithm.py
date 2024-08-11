
def find_coins_greedy(amount, coins):
    if amount == 0:
        return {0}

    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count

        amount = amount - (count * coin)
    return result


def find_min_coins(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    coins_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coins_used[i] = coin

    result = {}
    while amount > 0:
        coin = coins_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
