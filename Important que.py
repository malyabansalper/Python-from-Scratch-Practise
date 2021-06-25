# --------------------------------------------------------
# reverse of a number
#
# n=int(input("Enter Number: "))
# s=0
# while(n>0):
#     r=n%10
#     s=s*10+r
#     n=n//10
# print ("Reverse of the number is: "+str(s)+" ")

# --------------------------------------------------------

# sum of digits of the given number


# q=0
# n=int(input("Enter Number: "))
# while(n>0):
#     r=n%10
#     q=q+r
#     n=n//10
# print("Sum of digits is: "+str(q))


# --------------------------------------------------------
# palindrome of a number

# n=int(input("Enter Number: "))
# m=n
# t=0
# while(n>0):
#     r=n%10
#     t=(t*10)+r
#     n=n//10
# if(t==m):
#     print("Number is Palindrome")
# else:
#     print("Reverse of the number is "+str(t)+" and the original number is: "+str(m))


# --------------------------------------------------------

# Codechef challenge(num reversal for numerous test cases)
#
# n=int(input())
# l=[]
# for i in range(n):
#     num=int(input())
#     s=0
#     while(num>0):
#         r=num%10
#         s=(s*10)+r
#         num=num//10
#     l.append(s)
# for i in l:
#     print(i)


# --------------------------------------------------------

# palindrome of a string

n = int(input())
l = []
for i in range(n):
    string = input()
    b = string[-1::-1]
    if string == b:
        l.append("YES")
    else:
        l.append("NO")
for i in l:
    print(i)
