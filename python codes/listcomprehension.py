list1=[[101,"nikhil",78], [102, 'Aniket', 77], [103, 'Aryaman', 67]]

def dataFinder(name):
    for x in list1:
        if name.lower()==x[1].lower():
            return x
    return []

#print in the form of matrix
for x in list1:
    for y in x:
        print(y, end=' ')
    print()

#find the data using name
name = input("Enter the name : ")
dataList =dataFinder(name)
print(dataList) 