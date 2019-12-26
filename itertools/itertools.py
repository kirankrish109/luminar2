# import itertools
# # counter = itertools.count(start=5,step=2)
# lst=[100,200,300,400]
# # counter = itertools.count(start= 5,step=2)
#
# daily_data=list(zip(itertools.count(5),lst))
# print(daily_data)
#
#
# counter = itertools.repeat(2,times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# # print(next(counter))
# sq=itertools.starmap(pow,[(0,2),(1,2),(2,2)])
# print(list(sq))
#
# ab=['a','b','c','d']
#
#
#
# result = itertools.combinations(ab,2)
# for item in result:
#     print(item)
# print("------------------")
# result = itertools.permutations(ab,2)
# for item in result:
#     print(item)
# print("------------------")
#
# num=[0,1,2]
# result=itertools.product(num,repeat=2)
# for item in result:
#     print(item)
#
# print("------------------")


result = itertools.chain(lst,num)


#islice
result= itertools.islice(range(10,1,5)


#compress

letters=['a','b','c','d']
selectors = ['']
