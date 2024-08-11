from algorithm import find_coins_greedy, find_min_coins
import timeit


def main():
    coins = [50, 25, 10, 5, 2, 1]
    result_view = find_coins_greedy(113, coins)
    print(result_view)

    result_view = find_min_coins(113, coins)
    print(result_view)

    cases = [([50, 25, 10, 5, 2, 1], 113)]

    functions = [find_coins_greedy, find_min_coins]

    for coins, cash_amount in cases:
        print(f"\nCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=10000)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))


if __name__ == "__main__":
    main()
