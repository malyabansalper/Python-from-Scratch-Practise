n=input("Enter list : ").split()
l=[]
for i in n:
    l.append(int(i))
k=int(input("Enter the elemnet to be found : "))
def linear_search(n,k):
    iterator = 0
    while iterator < len(n):
        if(n[iterator]== k):
            return iterator
        iterator = iterator +1
    return -1
index=(linear_search(l,k))
if(index==-1):
    print("Element not found ")
else:
    print("Element found at index {0}".format(index+1))
