# counting number of 1 in a row 

def counting(s):
    max_c=0
    row=0
    for i in range(4):
        count=0
        for j in range(4):
            if s[i][j] == 1:
                count +=1
        if count>max_c:
            max_c=count
            row=i
    return row+1
               
                 



si=[[0,1,1,1,],
    [0,0,1,1],
    [0,0,0,1],
    [1,1,1,1]]

counting(si)

for i in range(4):
    for j in range(4):
        print(si[i][j] ,end=" ")
    print()

print(f"row with max no. of 1's is {counting(si)}")
