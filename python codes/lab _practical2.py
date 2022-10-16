# create a string made of midle three character of the given sring ?
s="hisamhi"
print(len(s))
mid=int(len(s)//2)
print(mid)
print(s[mid-1:mid+2])

# take a input string and apply the below string operations show the change in output
# lower,upper,islower,isupper,startswith,endswith,join,split,rjust,ljust,center,lstrip,rstrip,reverse 
name=" Nikhil Kumar  "
print(name.lower())
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.startswith(" Ni"))
print(name.endswith("ar  "))
print("<".join("'i','am','nikhil'"))
print(name.split(" "))
print(name.rjust(3))
print(name.center(20))
print(name.lstrip())
print(name.rstrip())
print(name[::-1])