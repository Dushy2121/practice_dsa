#midle element of three number

def middle(s1,s2,s3):
    x=[]
    x.append(s1)
    x.append(s2)
    x.append(s3)
    #print(x)
    highest=x[0]
    #print(highest)
    for i in range(0,len(x)):
        if(x[i-1]>x[i]):
            temp=x[i-1]
            x[i-1]=x[i]
            x[i]=temp
    print(x)


n1=int(input("first number "))
n2=int(input("second number "))
n3=int(input("third number "))
middle(n1,n2,n3)