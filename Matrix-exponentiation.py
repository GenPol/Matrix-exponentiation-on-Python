lst1 = []
lst2 = []
lst3 = []
s = 0
n = int(input('How many rows you want?'))
for i in range(n):
    if i != n-1:
        lst1.append(input('enter with space separated').split())
    if i == n - 1:
        lst1.append(input('last raw what you entering').split())
m = len(lst1[0])

N = int(input('Enter exponentiation:'))-1

n1,m1 = n, m
for i in range(n1):
    lst2.append([])
    for j in range(n1):
        lst2[i].append(lst1[i][j])

for h in range(N):
    for i in range(n):
        lst3.append([])
        for j in range(m1):
            for x in range(n1):
                s = s + (int(lst1[i][x])*int(lst2[x][j]))
            lst3[i].append(s)
            s = 0
    for k in range(n):
        for l in range(m):
            lst1[k][l] = lst3[k][l]
    lst3 = []

for i in range(n):
    print(*lst1[i])