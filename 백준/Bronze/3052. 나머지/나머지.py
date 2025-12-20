a = []
for _ in range(10):
    a.append(int(input().strip()) % 42)
b = []
for i in a:
    if i not in b:
        b.append(i)
print(len(b))