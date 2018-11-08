print('Simple Assignment')
shoplist = ['apple', 'orange', 'carrot', 'banana']
mylist = shoplist
print('origin shoplist is ', shoplist)

del shoplist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)












