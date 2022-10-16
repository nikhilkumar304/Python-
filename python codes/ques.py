# list1=[]
# def fun(*numbers):
#     for number in numbers:
#         if (number.isnumeric()):
#             list1.append(number)
#         else :
#            print(number+" is not a number")
#     list1.sort()
#     print(list1)
#     print("the second largest element of a list is "+list1[-2])
# fun('4','5','6','7',"hello")

from collections import defaultdict
test_list=[4,6,6,4,2,2,4,4,8,5,8]
res=defaultdict(list)
for ele in test_list:
    res[ele].append(ele)
print(str(dict(res)))
# n=7
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         if k==0 or k==2*i :
#             print("*",end='')
#         else:
#             if i==n-1:
#                 print("*",end='')
#             else:
#                 print(' ',end='') 
#     print()
# n=12
# for i in range(1,n+1):
#     for j in range(0,i):
#        print(" ",end='')
#     for k in range(1,(n*2-(2*i-1))+1):
#         if i==1 or k==1 or k==(n*2-(2*i-1)) :
#             print("*",end='')
#         else:
#             print(' ',end='') 
#     print()

            