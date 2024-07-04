n, m = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(n)]

for j in range(m):
    mx = float("-inf")
    s = 0
    for i in range(n):
        mx = max(mx, mat[i][j])
        s += mat[i][j]
    avg = s / n
    if mx - avg > mat[0][j]: 
        for i in range(n): 
            mat[i][j] = 1
print()
for el in mat: 
    print(*el)
    
