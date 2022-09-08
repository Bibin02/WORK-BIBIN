'''
        PRINTING Spiral number pattern (for n=4)
        1  2  3  4
       12 13 14  5
       11 16 15  6
       10  9  8  7

'''
n=int(input())
l=[[0 for i in range(n)] for i in range(n)]
r,x=0,1
while(True):
    for i in range(r,n-r):
        l[r][i]=x
        x+=1

    for j in range(r+1,n-r):
        l[j][n-r-1]=x
        x+=1

    for k in range(n-r-2,r-1,-1):
        l[n-r-1][k]=x
        x+=1

    for m in range(n-r-2,r,-1):
        l[m][r]=x
        x+=1
    r+=1
    if r==round(n/2):
        if (round(n/2))%2==0:
            l[m][r]=x
        break
for i in l:
    print(i)
