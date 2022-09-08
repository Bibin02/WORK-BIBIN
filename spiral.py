def iseven(num):
    flg=0
    if(num%2==0):
        flg=1
    return flg

n=int(input())
l=[[0 for i in range(n)] for i in range(n)]
r=0
x=1
a=1
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
        if iseven(round(n/2)):
            l[m][r]=x
        break
for i in l:
    print(i)