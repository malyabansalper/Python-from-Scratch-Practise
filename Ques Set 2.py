# Que 1. print all the natural numbers from 1 to n (user input). Then print the same in reverse order

# n=int(input("Enter a natural number: "))
# print("Numbers in ascending order are as follows: ")
# for i in range(1,n+1):
#     print(i,end=" ")
# print()
# print("Numbers in descending order are as follows: ")
# for i in range(n,0,-1):
#     print(i,end=" ")
# print()

#Que 2.Print all odd numbers and even numbers between 1 to 100

# for i in range(0,101):
#     if(i%2!=0):
#         print(i)
#     else:
#         pass

#Que 3. check if a number is prime or not. Example: 7 ==> True, 6 ==> False
#
n=int(input("Enter number to check if prime or not :"))
s=0
for i in range(2,n):
    if(n%i==0):
        s=s+1
if(s>0):
    print(False)
else:
    print(True)

#Que 4.
