import cmath
import constant
import math
from collections import OrderedDict
# 1.maximum length of identifier in python is 79 character.
# 2. variable name should start with lowercase letter or _(underscore),it should not start with a number,
#    it doesnot contain any special character other than _ ,they are case sensitive,var name must not be any keyword
# 3.
a=12
x=a>>2
print(x)
y=a<<1
print(y)
# 4. what is the use of indentation
# python uses indentation to indicate block of code,refers to the spaces in the beginning of a line of code 
# python indentation is a way of telling the interpreter that the group of statements
# belongs to a particular block of code .

# 5.
print(1+2*float(3)/4-5)

6. how are complex number represent in python.
.complex number is represented as real part and imaginary part such as(4+5j).
python can handle complex numbers and its associated function is in cmath.
python convert real numbers x and y into complex using function complex(x,y).
x,y=5,4
z=complex(x,y)
print(z)

7.how to define constant in python.
make a file with name constant and declare any constant value such as PI = 3.14 
then import constant in any file and use the value of PI by calling the variable with filename
print(constant.PI)


8.to calculate the area of triangle ny heron's formula
a,b,c=12,6,9
s=(a+b+c)/2
print("the value of s :",s)
Area_of_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("{0:.3f}".format(Area_of_triangle))
print(round(Area_of_triangle,2))

9.
list=[1,2,3,4,5,6,7,8,9]
print(list[3:9])# [4,5,6,7,8,9]
print(list[3:9:2])#[4,6,8]
print(list[3:9:3])#[4,7]
print(list[3:9:8])#[]
print(list[9:11])#[]
print(list[::2])#[1,3,5,7,9]
print(list[::4])#[1,5,9]
print(list[::])#[1,2,3,4,5,6,7,8,9]
print(list[::-1])#[9,8,7,6,5,4,3,2,1]
print(list[::-3])#[9,6,3]
print(list[:1:-2])#[9,7,5,3]
print(list[1:1:1])#[]

10.
li=[]
li=[int(item) for item in input("enter values of list :").split()]
print(li)
def countoccur(li):
    for i in li:
        print("repeating",i,"times :",li.count(i))
   
countoccur(li)
def evenoccur(a):
    k=[]
    for i in a:
        if i%2==0:
            k.append(i)
    k=list(OrderedDict.fromkeys(k))        
    print(k)  
evenoccur(li)

def oddoccur(a):
    k=[]
    for i in a:
        if (i%2)!=0:
            k.append(i)
    k=list(OrderedDict.fromkeys(k))
    print(k)
oddoccur(li)
11. read radius from user of circle and side of square using single input().then calculate area of circle and square

radius,side=input("enter the radius of circle:\n enter the side of square:").split()
radius=int(radius)
side=int(side)
def areaofCircle(rad):
    n=3.14*(rad*rad)
    return n
area_of_circle = areaofCircle(radius)
print("Area of circle :",area_of_circle)
def areaofsquare(side):
    return side*side
area_of_square = areaofsquare(side)
print("Area of square",area_of_square)

12.lower(),upper(),startswith(),join(),split(),rjust(*),center(),lstrip()
name=" Nikhil Kumar  "
print(name.lower())
print(name.upper())
print(name.startswith(" Ni"))
print("<".join("'i','am','nikhil'"))
print(name.split(" "))
print(name.rjust(3))
print(name.center(20))
print(name.lstrip())

13. write a program to check the number is panlindrome or not
num=int(input("enter the number to check it is palindrome or not :"))
reversednum=0
temp=num
while num>0:
    n=num%10
    reversednum=reversednum*10+n  
    num=num//10
if reversednum==temp:
    print("it's a palindrome number")
else:
    print("OOps!! it's not a palindrome number")

14.check wheather the number is prime or not
num=int(input("enter a number to check it is prime or not : "))
i=2
k=0
while i<num:
   if num%i==0:
       k=1
       break
   i=i+1
if k==0:
     print("its prime")
elif k==1:
     print("not prime")

