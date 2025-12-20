while True:
    s = list(map(int, input().split()))
    if s == [0, 0, 0]:
        break
    s.sort()
    x, y, z = s
    if x*x + y*y == z*z:
        print("right")
    else:
        print("wrong")
