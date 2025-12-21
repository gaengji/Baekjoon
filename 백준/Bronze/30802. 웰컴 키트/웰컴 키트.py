n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

tshirt = sum((x + t - 1) // t for x in sizes)
print(tshirt)

print((n // p), (n % p))
