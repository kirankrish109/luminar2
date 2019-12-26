lst=[1,2,3,4,5]
lst=list(map(lambda no:no*no,(filter(lambda no:no%2==0,lst))))
print(lst)