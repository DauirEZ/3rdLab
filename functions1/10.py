def l(x : list):
    for i in x:
        for j in range(0, i):
            if x[i] == x[j]:
                continue
            if i == j:
                k = x[i]
    print(k)
    
x = [1, 1, 2, 3]
            