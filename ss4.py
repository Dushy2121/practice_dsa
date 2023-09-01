# finding the number of perfect square (blow the key given :
import math 
def perfect(s):
    a=int(math.sqrt(s))-1
    return a


n=int(input(" enter the number"))

perfect(n)
print(perfect(n))