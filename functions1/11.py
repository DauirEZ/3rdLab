def p(k : list):
    k1 = k.reverse()
    for i in range(len(k)):
        if(k1[i] == k[i]):
            print("Yep")
        else:
            print("Nope")
            
p(["AabaA"])
    