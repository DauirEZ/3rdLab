def h(my_list): 
    for i in my_list:
        for j in range(i):
            print("*", end = "")
        print()
        
h([4, 7, 9])