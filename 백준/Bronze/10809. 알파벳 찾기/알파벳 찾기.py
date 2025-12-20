S = input().strip()

for c in range(ord('a'), ord('z') + 1):
    print(S.find(chr(c)), end=' ')