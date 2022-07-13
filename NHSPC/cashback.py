for test_case in range(int(input())):
    c = int(input())
    outs = []
    mxy = []
    for i in range(c):
        mxy.append(list(map(float, input().split())))
    _ = input()
    s = sum(list(map(float, input().split())))
    for i in range(c):
        m, x, y = mxy[i]    
        if s > m:
            outs.append(s / 100 * x)
        else:
            outs.append(s / 100 * y)

    print(outs)