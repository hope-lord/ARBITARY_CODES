
import numpy as np
sd=[[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]
'''sd=[[0,2,0,0,5,1],
    [1,0,0,6,0,0],
    [0,3,1,0,4,0],
    [2,0,3,0,1,0],
    [0,1,5,0,6,0],
    [4,0,0,5,0,3]]'''
sd=np.array(sd)
print(sd,"\n \n")
def possible(y,x,n,no):
    global sd
    for i in range(no):
        if sd[y][i]==n:
            return False
    for i in range(no):
        if sd[i][x]==n:
            return False
    x0=int(x/3)
    y0=int(y/3)
    for j in range(y0*3,y0*3 +3):
        for k in range(x0*3,x0*3 +3):
            if sd[j][k]==n:
                return False
    return True
def solve(no=9):
    global sd
    for y in range(no):
        for x in range(no):
            if sd[y][x]==0:
                for n in range(1,no+1):
                    if possible(y,x,n,no):
                        sd[y][x]=n
                        solve(no)
                        sd[y][x]=0
                return
    print(sd)
#it by defult solve 9X9 sudoku.
#if you want to solve 6X6 feed 6 in solve below
solve()


