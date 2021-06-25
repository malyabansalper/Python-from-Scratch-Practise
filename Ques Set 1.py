
# Que 1.compute roots of a quadratic equation when coefficients a, b and c are known(entered by user). (Without using math module)

# print("Equation a* x^2 + bx +c =0")
# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# c=int(input("Enter value of c: "))
#
# z= (b**2)-(4*a*c)
# if(z>0):
#     x1 = (((-b) + (z**0.5)) / (2 * a))
#     x2 = (((-b) - (z**0.5)) / (2 * a))
#     print("The roots of the quadratic equation are %.2f and %.2f :" % (x1,x2))
# elif(z==0):
#     x=(-b)/(2*a)
#     print("The root is : "+str(x))
# else:
#     print("OOPS! There are no real roots as discriminant is less than zero.")



# Que 2. Volume of Sphere

# import math
#
# r=int(input("Enter radius of the sphere: "))
# volume=str("{:.2f}".format((4/3)*(math.pi * (r**3))))
# print("Volume of the sphere is "+volume)

# Que 3. Count number of digits in a number

# n=int(input("Enter Number whose digits are to be counted : "))
# s=0
# while(n>0):
#     r=n%10
#     s=s+1
#     n=n//10
# print(s)


# Que 4. accepts two strings and outputs the concatenation of them
#
# n1=input("Enter first String : ")
# n2=input("Enter second String : ")
# print(n1+n2)


# Que 5. accepts a string and gives output string with all capital letters
#
# n=input("Enter string whose letters are to be capitalized : ")
# print("String in uppercase: "+n.upper())
# print("First letter uppercase: "+n.capitalize())
# print("String in lowercase: "+n.lower())

# Que 6. accepts a string s, an index number n and a character. And outputs the string replaced with the character at the index number n

# s=input("Enter String : ")
# l=list(s)
# snew=[]
# n=int(input("Enter number at which character is to be replaced: "))
# char=input("Enter the character to replace with: ")
# for i in range(0,len(l)):
#     if(i==(n-1)):
#         snew.append(char)
#     else:
#         snew.append(l[i])
# print("".join(snew))


# Que 7. Reverse a string
#
n=input("Enter string to be reversed: ")
a=n[::-1]
print(a)


