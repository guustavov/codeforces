if __name__ == "__main__":
    line = raw_input()
    a, b, c =  (int (s) for s in line.split())

    best = 0
    for i in range(0, 7):
        ax = a
        bx = b
        cx = c
        days = 0
        
        j = i

        while(True):
            j = j % 7
            if(ax > 2 and bx > 1 and cx > 1):
                ax -= 3
                bx -= 2
                cx -= 2
                days += 7
                j += 7
            else:
                if(j == 2 or j == 6):
                    if(bx == 0):
                        break
                    bx -= 1
                elif(j == 3 or j == 5):
                    if(cx == 0):
                        break
                    cx -= 1
                else:
                    if(ax == 0):
                        break
                    ax -= 1
                days += 1
                j += 1

        if(days > best):
            best = days

    print(best)

    