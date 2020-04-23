from itertools import combinations
import matplotlib.pyplot as plt
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1 
# print(coinChange([1,2,3], 10))
List = list(combinations([1,2,3,4],3))
legends = []

for coins in list(combinations([i for i in range(2,10)],2)):
    coins = list()
# for coins in [[1,2,5,10,20,50,100,200]]:
    legends.append(str(coins))
    printMoney = []
    for m in range(1, 20):
        printMoney.append(coinChange(coins, m))
    
    print(coins, ':', printMoney[-1], sum(printMoney))

    plt.plot(printMoney)
    
plt.legend(legends)
plt.show()