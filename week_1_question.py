# Write a Python program to swap two variables. 
# a=1
# b=2
# print(a,b)
# c=a
# a=b   #a,b = b,a
# b=c
# print(a,b)

# Take user input and display it back to the user. 
# i= input()
# print(f"your input is {i}")

#Write a program to check if a number is even or odd. 
# n = int(input("Enter a number : "))
# if n%2==0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")

# Create a program that prints the multiplication table of a given number.
# n= int(input("Enter a number to print its multi-table : "))
# for i in range(1,11):
    # print(f"{n}X{i}={n*i}")

#Write a program to find the largest of three numbers.
# a=int(input("enter 1st number to compare : "))
# b=int(input("enter 2nd number to compare : "))
# c=int(input("enter 3rd number to compare : "))
# if a>b and b>c:
#     print(f"{a} a is the greatest")
# elif b>a and b>c:
#     print(f"{b} b is the greatest")
# else:
#     print(f"{c} c is the greatest")

# Convert temperature from Celsius to Fahrenheit.
# c= float(input("Enter temperature in celcius "))
# f=(((c*9)/5)+32)
# print(f"Temperatuer in fahrenheit is {f}*F")

#Write a program to calculate the factorial of a number using a loop.
# n=int(input("Enter a number to find its "))
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# print(f"factorial of {n} is {fact}")

# Create a program to count the number of vowels in a string.
# c=0
# n= input("enter a string  ")
# v="AEIOU"
# for i in range (len(n)):
#     for k in range (len(v)):
#         if (n[i]).upper()==v[k]:
#             c=c+1
#         else:
#             continue
# print(f"the no of violes are {c}")

#Write a Python script to reverse a given string. 
# a= input("enter a string: ")
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# Check if a number is a palindrome.
# n= int(input("Enter a no to check if it is palindrome "))
# rev=0
# c=n
# while c>0:
#     r=c%10
#     rev=rev*10+r
#     c=c//10
# if n==rev:
#     print(f" {n} is a penlindrome no.")
# else:
#     print(f" {n} is  not a penlindrome no.")

# Write a program to find the sum of first N natural numbers.
# N= int(input("enter a number : "))
# n=0
# for i in range (1,N+1):
#     n=n+i
# print(f"sum of n natural no is {n}")

#Create a number guessing game. 
# import random
# t=0
# n=random.randint(1,100)
# while True:
#     g= int(input("guess the  number between 1 to 100 :"))
#     t+=1
#     if g==n:
#         print(f"you are right with {t} tries")
#         break
#     elif g>n :
#         print("go a bit smaller")
#     elif g<n :
#         print("go a bit larger")
#     else:
#         print("sorry you are wrong")

#Write a program to print all prime numbers between 1 and 100.
# for i in range (1,101):
#     c=0
#     for k in range (1,i+1):
#         if i%k==0:
#             c=c+1
#         else:
#             continue
#     if c==2:
#         print(f"{i} is a prime number")
#     else:
#         continue

# Check if a given year is a leap year or not.
# y=int(input("Enter the year"))
# if y%100==0 and y%400==0:
#     print(f"{y} is leap year")
# elif y%100!=0 and y%4==0:
#     print("leap year")
# else:
#     print("normal year")

# Create a program to print the Fibonacci series up to N terms.
# n= int(input("enter a no "))
# a=0
# b=1
# for i in range (n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#Write a program to find the GCD of two numbers.
# a=int(input("enter 1st a number "))
# b=int(input("enter 2nd a number "))
# if a<b:
#     er=a
#     end=b
# else:
#     er=b
#     end=a
# while er!=0:
#     r=end%er
#     end=er
#     er=r
# print("gcd is ",end)

#Write a program to find the LCM of two numbers.
# a=int(input("enter 1st a number "))
# b=int(input("enter 2nd a number "))
# n=1
# if a<b:
#     s=a
#     g=b
# else:
#     s=b
#     g=a
# while True:
#     if g%a==0 and g%b==0:
#         break
#     g=g+1
# print(f"LCM is {g}")

#Check whether a character is a vowel or consonant. 
# w= input("enter a character ")
# u=w.upper()
# if u=="A"or u=="E"or u=="I"or u=="O"or u=="U" :
#     print("vowel")
# else:
#     print("consonant")

#Write a program to calculate the sum of digits of a number. 
# n=int(input("enter a number "))
# t=n
# c=0
# while t>0:
#     r=t%10
#     t=t//10
#     c+=r
# print(f"sum of digit is {c}")

#20.Create a program to find the second largest number in a list. 
# li=(input("enter the list :")).split(" ")
# numli=[int(x) for x in li]
# numli.sort()
# print(numli[-2])

#Write a program to count the number of digits in an integer.
# n=int(input("enter a number "))
# t=n
# c=0
# while t>0:
#     t=t//10
#     c+=1
# print(f"sum of digit is {c}")

#Create a program to print all Armstrong numbers between 1 to 1000. 
# for i in range (1,1001):
#     c=0
#     t=i
#     while t>0:
#         t=t//10
#         c+=1
#     t=i
#     p=0
#     while t>0:
#         r=t%10
#         t=t//10
#         p+=(r**c)
#     if p==i:
#         print(f"armstrong number is {p}")

#Write a Python program to print a pattern of stars in a triangle. 
# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#     print("*" * i,end="\n")

#Create a calculator app using if-else.
i=0
while i!= -1:
    a=int(input("Enter 1st number :"))
    o=input("Enter operator :")
    b=int(input("Enter 2nd number :"))
    if o=="**":
        print(a**b)
    elif o=="/":
        print(a/b)
    elif o=="//":
        print(a//b)
    elif o=="":
        print(a//b)
    elif o=="%":
        print(a%b)
    elif o=="*":
        print(a*b)
    elif o=="+":
        print(a+b)
    elif o=="-":
        print(a-b)
    else:
        print(f"{o} this operator is not include")
    i= int(input("enter 1 to play again -1 to break"))
else:
    print("THANK YOU")
#Write a program to display the ASCII value of a character.
# n = input("Enter character: ")
# p=ord(n)
# print(ord(n))

#Convert a decimal number to binary using loops. 
# num=int(input("enter a decimal number:"))
# b=0
# n=num
# while n!=0:
#     r = n%2
#     b=b*10+r
#     n=n//2
# print(f"binary of {num} is {b}")

#Create a program to find the square root of a number.
# n = int(input("Enter number: "))
# print("square root is",n**1/2)

# Write a program to find the sum of all even numbers in a list.
# n = int(input("Enter number: "))
# c=0
# for i in range(1, n + 1):
#     if i%2==0:
#         c=c+i
# print("sum of even no.s are",c)

#Create a program to check whether a number is prime or not
# n = int(input("Enter number: "))
# c=0
# for i in range (1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print(f"{n} is a prime no")
# else:
#     print(f"{n} is not a prime no")

#Write a program to display the cube of the number up to an integer.
# n = int(input("Enter an integer: "))
# for i in range(1, n + 1):
#     print(f"Cube of {i} is {i**3}")
