#searching for number in matrix 

def search(s,x):
    for i in range(0,4):
        for j in range(0,4):
            if (s[i][j] == x):
                print(f"yes the number is present in matrix position is {i},{j}")
                i+=1
                j+=1
                return 1
            else:
                print(f'number is not present ')
                return 0
     



si=[[11,25,42],
    [51,6,1],
    [8,12,45]]

for i in range(0,3):
    for j in range(0,3):
        print(si[i][j] , end=" ")
    print()

xi=int(input("number you want\n"))

search(si,xi)