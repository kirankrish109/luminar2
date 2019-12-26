lst1 = [1,2,3]
lst2 = [4,5,6]

lst3=[(i,j) for i in lst1 for j in lst2]
print(lst3)


#_________________________________________________________


lst4=[(i+j) for i in lst1 for j in lst2]
print(lst4)

#############################################################

#squre of the number of list



lst5= [(i**2) for i in lst1]
print(lst5)


lst6 = [(i) for i in lst1 if i%2==0]
print(lst6)




