def minimumLoss(prices):
    min_,length = float("inf"),len(prices)
    for i in range(length):
        for j in range(i+1,length):
            if prices[i]>prices[j]:
                min_ = min(min_,prices[i]-prices[j])
    return min_

print(minimumLoss([20,7,8,2,5]))