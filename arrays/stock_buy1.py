def stock_buy(prices):
    profit = 0
    buy_min = prices[0]

    for i in range(1, len(prices)):
        buy_min = min(buy_min, prices[i])
        # if prices[i] < buy_min:
        #     buy_min = prices[i]
        profit = max(profit, prices[i] - buy_min)
        # if (prices[i] - buy_min) > profit:
        #     profit = prices[i] - buy_min
    
    return profit

print(stock_buy([7,1,5,3,6,4]))