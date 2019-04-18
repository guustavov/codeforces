import itertools as it

if __name__ == "__main__":
    n = int(raw_input())

    students = []
    for i in range(n):
        line = raw_input()
        a, b =  (int (s) for s in line.split())
        students.append([a, b])

    arrangements = it.permutations(students, r=n)

    minimum = 99999999
    for a in arrangements:

        total = 0
        for j in range(n):
            d = a[j][0] * ((j+1) - 1) + a[j][1] * (n - (j+1))
            total += d

        print(total)

        if (total < minimum):
            minimum = total

    print(minimum)