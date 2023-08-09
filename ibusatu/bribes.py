def minimumBribes(q):
    bribes = 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print ("Too chaotic")
            return

        print(list(range(max(0, q[i] - 2), i)))
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

minimumBribes([2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10, 14, 13, 12, 17, 16, 15, 19, 18, 20])