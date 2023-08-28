#string reversal 

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
strr=input("input string")
print("the string is "+strr)
print("the reversed string is "+reverse(strr))