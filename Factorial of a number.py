# n=int(input("Enter Number : "))
n=5
# Iterative Method
def fact(n):
    p=1
    while n>0:
        p=p*n
        n=n-1
    return p

# Recursive Method
def recursiveFact(n):
    if n==1:
        return 1
    else:
        return recursiveFact(n-1)*n

print(recursiveFact(n))
print(fact(n))