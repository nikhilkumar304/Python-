# 8).write a program to accept a num from the user and calculate sum of all the integer upto that number ?/ 
# num=int(input("enter the number:"))
# sum=0
# for i in range(1,num+1):
#    sum=sum+i
# print(sum)

#9).write a program to print multiplication table of the num ?
# num= int(input("enter the number for table :"))
# for i in range(1,11):
#    sum=num*i
#    print(num,"*",i,"=",sum)

#10).write a program to display only those number from a list  the satisfy the following conditions?
# the number must be divisible by 5
# if the number is greater than 150 then skip it and move to the next number
# if the number is greater than 500 then stop the loop  
# li=[12,75,150,180,145,525,50]
# for i in li:
#    if i>500:
#       break
#    elif i>150:
#       continue
#    elif i%5==0:
#       print(i)
#
#!!).write a program to check the string is palindrome or not using function.
# str=input("enter a string to check palindrome or not : ")
# reversestr=str[::-1]
# def palindrome(str):
#        if reversestr==str:
#               print("its palindrome")
#        else:
#               print("not a palindrome")
# palindrome(str)

#12).write a program to check wheather a number is prime or composite or even or odd.
num=int(input("enter a number to check (prime or composite)&(even or odd): " )) 

def primecomposite(num):
  r=0 
  k=2
  while k<num:
      if num%k==0:
        r=1
        break
      k=k+1
  if r==1:
      print("composite")
  elif r==0:
      print("prime")
primecomposite(num)
def evenodd(num):
   if num%2==0:
      print("even")
   else:
      print("odd")
evenodd(num)