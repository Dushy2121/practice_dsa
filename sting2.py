# checking if palindrome or not 

def palindrome(s):
    e=0
    l=len(s) -1
    for i in s:
        if s[e] == s[l]:
            e=+1
            l=-1
            return print('it is a palindrome number ')
        else:
            return print('it is not a palindrome number ')

si=[]
si=input('enter the string\n')
palindrome(si)