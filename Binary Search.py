n=input("Enter the list : ").split()
k=int(input("Enter elemnet to be found : "))
l=[]
for i in n:
    l.append(int(i))

# Iterative Approach
def binarySearch(arr,k):
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2
        if(k==arr[mid]):
            return mid
        elif k<arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1

# Recursive Approach
def binaryRec(ar,f,start,end):
    if start> end:
        return -1
    else:
        mid=(start+end)//2
        if(f==ar[mid]):
            return mid
        elif f<ar[mid]:
            return binaryRec(ar,f,start,mid-1)
        else:
            return binaryRec(ar,f,mid+1,end)


print(binaryRec(sorted(l),k,0,len(l)-1)+1)
print(binarySearch(sorted(l),k)+1)


