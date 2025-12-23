n = int(input())
a = list(map(int, input().split()))

n = 0
for x in a:
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            n += 1

print(n)
