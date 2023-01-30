def minimum_coin( v ):
    den = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

    ans_arr = []

    for i in range(len(den)-1, -1, -1):
        while v >= den[i]:
            v -= den[i]
            ans_arr.append(den[i])
    
    return len(ans_arr), ans_arr

print(minimum_coin(27))