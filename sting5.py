# checking count and say sequence problem 

def check(n):
    if (n==1):
        return print("1") # if n==1
    if (n==2):
        return print('11') # if n==2
    s='11'
    for i in range(3,n+1): # as n=1,2 is done so the loop starts from 3 
        s+="&"
        c=1
        t=''                
        for j in range(1,len(s)):#eg 1211 2==j 1==j-1 therefore loop starts from 1
            if(s[j]!=s[j-1]):
                t= t+str(c) #adding the count 
                t=t+s[j-1] # adding the number
                c=1 # if number is diff then just add the count to empty  string 
            else:
                c=c+1 #increment of count if the next number is same 
        s=t
    return (s)
ni=int(input('number of rows '))
print(f"{check(ni)}\n")