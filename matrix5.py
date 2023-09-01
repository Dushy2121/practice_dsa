# sorted matrix

def sorted(si):
    sorted=[]
    n= len(si)
    for i in range(n):
        for j in range(n):
            sorted.append(si[i][j])
    #return print(x)       

    sorted.sort()
    k=0
    for i in range(3):
        for j in range(3):
            si[i][j]=sorted[k]
            k +=1

    for i in range(3):
        for j in range(3):
            print(si[i][j] ,end=" ")
        print("")



s=[[1,3,2],
   [4,6,5],
   [7,9,8]]

sorted(s)
