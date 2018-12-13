#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
def edit_distance(s1, s2):
    x=len(s1)+1
    y=len(s2)+1

    tbl = {}
    for i in range(x): tbl[i,0]=i
    for j in range(y): tbl[0,j]=j
    for i in range(1, x):
        for j in range(1, y):
            if s1[i-1] == s2[j-1]:
               cost = 0
            else:
                cost = 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]
print('the minimun number of operations is :')
print(edit_distance("miners", "mo"))