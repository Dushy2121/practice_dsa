# spiral tranversal matrix  checking 

def tranversal(si):
    rowend=len(si)
    rowbegin=0
    columnbegin=0
    columnend=len(si[0])
    r=[]

    while rowbegin<rowend  and columnbegin<columnend:
        for i in range(columnbegin,columnend):
            r.append(si[rowbegin][i])
        for j in range (rowbegin +1,rowend -1):# rowend =3(length of matrix) and we want 2,2
            r.append(si[j][columnend -1])#columnend=3 and we want 2
        
        if rowbegin != rowend:
            for i in range(columnend -1,columnbegin -1,-1):
                r.append(si[rowend -1][i])
        if columnbegin != columnend:
            for i in range(rowend -2, rowbegin,-1):#column 1 down to up therefore 2 last row therefore -2
                    r.append(si[i][columnbegin])
        rowbegin +=1
        rowend -=1
        columnbegin +=1
        columnend -=1
    return print(r)




s=[[1,2,3,4]
   ,[2,3,4,5]
   ,[3,4,5,6]
   ,[4,5,6,7]]

for i in range(0,4):
    for j in range(0,4):
        print(s[i][j] , end =" ")
    print()

tranversal(s)










'''
elem=[]
for i in range(0,3):
    print(f'row is {i}')
    for j in range(0,3):
        ele=int(input(''))
        elem.append(ele)
    si.append(elem)
#print(si)

for i in range(3):
    for j in range(3):
        e=si[i][j]
        print( e,end=" ")
    print()
    '''