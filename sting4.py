#check whether a string is a valid shuffle of two strings or not
#check if string 1  is present in string 2
#eg: str1=hellohibye  str2=heyhellohitwobye

def check(str1,str2):
    if len(str1)>len(str2):
        return print('string 1 is not present in string 2')
    elif len(str1)<len(str2):
        if (str2.find(str2)!=-1):
            return print("string 1 is present in string 2")
    else:
        return print('string 1 is not present in string 2')

s1=input('string 1\n')
s2=input('string 2\n')

check(s1,s2)
