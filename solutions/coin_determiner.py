"""
For this challenge you will be determining the smallest combination of coins for a given output.

Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250,
and return an integer output that will specify the least number of coins, that when added, equal the
input integer. Coins are based on a system as follows: there are coins representing the integers 1, 5,
7, 9, and 11. So for example: if num is 16, then the output should be 2 because you can achieve the
number 16 with the coins 9 and 7. If num is 25, then the output should be 3 because you can achieve 25
with either 11, 9, and 5 coins or with 9, 9, and 7 coins.
"""


def CoinDeterminer(num: int):
    coins = [1, 5, 7, 9, 11]
    if num == 0:
        return 0
    # queue for bfs where [[node, step]]
    queue = [[0, 0]]
    visited = {0}
    for node, step in queue:
        for coin in coins:
            if node + coin in visited:
                continue
            if node + coin == num:
                return step + 1
            elif node + coin < num:
                queue.append([node + coin, step + 1])
                visited.add(node + coin)
    return -1


print(CoinDeterminer(25))
