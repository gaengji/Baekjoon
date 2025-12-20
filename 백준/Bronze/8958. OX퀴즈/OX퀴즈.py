t = int(input())

for _ in range(t):
    a = input().strip()
    n = 0 
    m = 0 
    for ch in a:
        if ch == 'O':
            n += 1
            m += n
        else:
            n = 0
    print(m)