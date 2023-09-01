# finding the medium of the matrix

def medium(s):
    l=round(len(s)/2)
    
    print(s[l])
    return 0


si=[]

for i in range(0,3):
    print(f'row number is {i}')
    for j in range(0,3):
        ele=int(input(""))
        si.append(ele)

print(si)
medium(si)