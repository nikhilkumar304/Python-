# 1.
# def student(name,subject):
#     print("Name: {} and subject: {}".format(name,subject))

# student("Nikhil","Computer Science")

# 2.
# def sum(a,b):
#     print("sum :",a+b)

# sum(10,20)

# 3.
# def calculation(a,b):
#     print("addition :",a+b)
#     print("subtraction:",b-a)
#     print("multiply :",a*b)

# calculation(10,20)

# 4.
# def recursivefunc(a):
#     if a<=1 :
#      return a 
#     return a + recursivefunc(a-1)

# print(recursivefunc(5))

# 5. 
# x=lambda a,b:a+b
# print(x(2,3))

# 6.
# import random
# print(random.randint(1000,5000))

# 7. 
# import random
# li=["a2cd3f","235bd3","5b67h4","1Aeh26"]
# print(random.choice(li))

# 8.
import random
li=["a2cd3f","235bd3","5b67h4","1Aeh26"]
random.shuffle(li)
print(li)