nMax = 5
n = int(input('Enter the number: '))
a = []
while len(a) < nMax:
    a.append(1.0/n)
    n = n + 1
print(a)