#checking is rotation string or not 
def rotation(s,v):
    if len(s) != len(v):
        return print('it is not a rotation string')
    else:
        concat=s+s
        if(concat.find(v)!=-1):
            return print("it is a rotation string")
        else:return print('it is not a rotation string')

si=input('1 string is \n')
vi=input('2 string is \n')

rotation(si,vi)