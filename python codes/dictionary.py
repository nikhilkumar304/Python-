dict={
    'brand':'oddy',
    'model':'yo43m',
    'year':1920
}
print(dict['model'])
print(len(dict))
print(dict.keys())
print(dict.values())
del dict['year']
print(dict)
dict['year']=1980
print(dict)
print('model' in dict)
print(dict.items())
dict.update({'year':1709})
print(dict)
print(dict.fromkeys(dict,0))
# create a string made of midle three character of the given sring ? 