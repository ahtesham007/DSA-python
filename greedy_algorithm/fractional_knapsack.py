class Item:
    def __init__(self, val, wt) -> None:
        self.val = val
        self.wt = wt

def fractional_knapsack(W, arr:Item, n):
    arr.sort(key=lambda x : x.val / x.wt, reverse = True)
    mp = 0
    for item in arr:
        if item.wt <= W:
            mp += item.val
            W -= item.wt

        else:
            mp += item.val / item.wt * W
            break
    
    return mp