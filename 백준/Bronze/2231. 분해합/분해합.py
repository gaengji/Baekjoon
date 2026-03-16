import sys

input = sys.stdin.readline

a = int(input())
i = 1

while True:
    if i == a:
        print(0)
        break
    
    j = str(i)
    n = sum(map(int, j))
    if i + n == a:
        print(i)
        break
    i += 1