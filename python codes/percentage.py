a=[]
n=int(input("number of subjects in your class:"))
print("enter marks :")
for i in range(n):
    a.append(int(input()))
print("marks :",a)
total=0
for i in range(n):
     total+=a[i]
print("total marks :",total)
percentage=0
percentage = (total/(n*100))*100
print("percentage is :",percentage)   

if (percentage>80):
    print("Grade:A+")
elif (percentage>70):
    print("Grade:A")
elif (percentage>65):
    print("Grade:B+")
elif (percentage>60 & percentage<65):
    print("Grade:B")
elif (percentage>55):
    print("Grade:C+")
elif (percentage>50):
    print("Grade:C")
else:
    print("Grade:D")
