# 13). write a program to calculate the area of traingle by using the herons formuala ?
# import math
# a, b, c= input("enter the length of sides of a traingle :").split()
# a=int(a);b=int(b);c=int(c)
# s =(a+b+c)/2
# area_triangle=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print('Area of Triangle : %.2f'%area_triangle)

# 14).write a program to calculate the distance between two points ?
# import math
# p1=input("enter the cordinates of first point: ").split(' ')
# print(p1[0],p1[1])
# p2=input('enter the cordinates of second point: ').split(' ')
# print(p2[0],p2[1])
# distance=math.sqrt((int(p2[0])-int(p1[0]))**2+(int(p2[1])-int(p1[1]))**2)
# print("Distance between two points are :%.2f"%distance)

#15). write a program to find the greatest among the 3 numbers
# a, b, c  = input("enter the  3 numbers to find greatest among them : ").split()
# a=int(a);b= int(b); c=int(c)
# if (a>b) and (a>c) :
#     print("greatest number is:",a)
# elif (b>a) and (b>c) :
#     print("greatest number is:",b)
# else :
#     print("greatest number is:",c)

# 16).write a program to convert farenherit to celsius?
# celsius= float(input("enter the temperature in celsius :"))
# farenheit= celsius *(9/5)+32
# print(farenheit)

#17).write a program to input from the user and check whether the input is character or number?
# user_input=input("enter the text: ")
# if(user_input.isdigit()):
#     print("it is numeric characters")
# else:
#     print("it is alphabet characters")

#18). write a program to calculate gcd of two number
# a=int(input("enter the first number: "))
# b=int(input("enter the second number: "))
# def compute_gcd(x,y):
#     while(y):
#         x,y =y,x % y
#     return x

# gcd=compute_gcd(a,b)
# print(gcd)

#19). write a program to find the average if the first n natural numbers?
# n=20
# def average(n):
#     sums=0
#     count=0
#     for i in range(1,n+1):
#         sums = sums + i
#         count=count+1
#     print(sums/count)
# average(n)

#20). write a program to find the factorial of a number using for loop?
# n=5
# fact=1
# for i in range(1,n+1):
#    fact=fact*i
# print(fact)

#21). write a program using while loop to read the numbers until -1 is encountered.
#     also find the number of prime numbers and composite numbers?

def check_number(n):
    if n>1:
        flag= True
        if n==2:
            return flag
        else:
            for i in range(2,n):
                if n%i==0:
                    return False
                else:
                    flag= True
            return flag
prime=composite=0
n= int(input("enter number: "))
while(n!=-1):
    if check_number(n):
        prime += 1
    else:
        composite +=1
    n= int(input("enter number: "))
print("Total prime numbers: ",prime)
print("Total composite numbers: ",composite)



