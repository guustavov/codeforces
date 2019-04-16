if __name__ == "__main__":
    line = raw_input()
    n, k = (int(s) for s in line.split())
    
    line = raw_input()
    x = []
    [x.append(int(s)) for s in line.split()]

    y = [0] * len(x)

    team = 0
    while(sum(x) <> 0):
        # index of max
        i = x.index(max(x))
        team = team % 2

        upper = i+k+1
        lower = i-k
        print(upper)
        print(lower)
        if(upper > len(x)):
            upper = len(x)
        if(lower < 0):
            lower = 0
        print(upper)
        print(lower)
        print("\n")

        indexes = [i for i in range(lower, upper) if y[i] == 0]
        for index in indexes:
            y[index] = team+1
        x[lower:upper] = [0] * (upper - lower)

        team += 1

    print("".join(str(w) for w in y))

