li=[1,2,[3,4,5],[6,7,8]]
newmax=[]
def removenesting(l):
	for i in l:
		if type(i)==list:
			removenesting(i)
		else:
		   newmax.append(i)
removenesting(li)
print(newmax)
