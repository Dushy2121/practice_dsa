# first and last occurrences of x 

def first(a,xi):
    count=0
    for i in range(len(a)):
        if (a[i]==x):
            count+=1        
            if (a[i+1]==x):
                print(f'first occurences of {xi} is {i+1}')
                return print(f'second occurences is {i+2}')

    print(f'number of {xi} is {count}')
            
            
    #print(f'the last occurance of {xi} is {i}')

ai=[1,2,3,3,4,5,5,2,1]
x=int(input("number you want"))
first(ai,x)
