# Value equal to index value

def value(arr):
    n=len(arr)
    for i in range(n):
        if arr[i] == i+1:
            print(f"only {arr[i]} is equal to the index ")
        #else:
            #print("there is no vlue which is equal to its index " )

a=[1,6,3,2,1,6]

value(a)