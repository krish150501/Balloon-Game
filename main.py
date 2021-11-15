def pop(mat):
    flag=False
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            count=1
            if(mat[i][j]=='-'):
                break
            for k in range(j+1,len(mat)):
                if(not mat[i][j]==mat[i][k]):
                    k-=1
                    break
                else:
                    count+=1
            if(count>2):
                flag=True
                for a in range(j,k+1):
                    mat[i][a]='-'
    return flag
def sot(mat):
    for j in range(len(mat)):
        for i in range(len(mat)):
            if(mat[i][j]=='-'):
                    for k in range(i,len(mat)-1):
                        mat[k][j]=mat[k+1][j]
                    mat[k+1][j]='-'

n=int(input())
mat = [['-' for i in range(n)] for j in range(n)]
flag=True
while(flag):
    x=int(input())
    m=input()
    k=x-1
    for i in range(len(m)):
        for j in range(n):
            if mat[j][k]=='-':
                mat[j][k]=m[i]
                break
        if(k<n-1):
            k+=1
        else:
            k=0
    for i in reversed(mat):
        print(i)
    while(pop(mat)):
        sot(mat)
    for i in reversed(mat):
        print(i)
    
    if(int(input())==0):
        flag=False
