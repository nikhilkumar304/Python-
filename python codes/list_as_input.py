# 1.WRITE a program to accept a list from the user as input and print alternate elements of list
    # list=input("enter the elements in list:")
    # List=list.split()
    # print(List)
    # print(List[1::2])

# 2.write a program to remove the element"3" from the given list[1,2,3,4,5.6]
    # NUM=[1,2,3,4,5,6]
    # NUM.remove(3)
    # print(NUM)
    
# 3. write a program to insert the element"python" on index 2 in the given list["java","php",".Net","Angular"]
    # list=["java","php",".Net","Angular"]
    # list.insert(2,"python")
    # print(list)
    
# 4. write a program to add elements in list using for loop
    # num=[]
    # n=int(input("the number of elements in a list"))
    # for i in range(0,n):
    #   ele=input()
    #   num.append(ele)
    # print(num)

# 5. write a program to perform slicing with tuple("python",1,2,3,"java",'A','B')
# * print alternate value of tuple
# * print value between index 1 to 5
# * print last value of tuple
    # print(tuple[1::2]) # alternate value
    # tuple=("python",1,2,3,"java",'A','B')
    # print(tuple[1:5])  # index value 1 to 5
    # print(tuple[-1])   # last elememts of tuple

# 6. write a program to count elements in given tuple(1,2,3,4,5,6,7,8)
    # tuple=(1,2,3,4,5,6,7,8)
    # x=tuple.count(3)
    # print(x)

# 7. write a program to convert tuple into list
    # tuple=(1,2,3,4,"python","java")
    # list=list(tuple)
    # print(list)

# 8. write a program to convert two given list into dictionary
# List1=[1,2,3,4,5] and List2['A','B','C',D','E']
    # List1=[1,2,3,4,5]
    # List2=['A','B','C','D','E']
    # print(dict(zip(List1,List2)))

# 9. write a program to print keys from the given dictionary{1:"Apple",2:"Banana",3:"Mango"}
dictionary={1:"Apple",2:"Banana",3:"Mango"}
print(list(dictionary.keys()))

# 10. write a program to print values from the given dictionary{1:"Apple",2:"Banana",3:"Mango"}
dictionary={1:"Apple",2:"Banana",3:"Mango"}
print(list(dictionary.values()))