words=open("passstd","r")
out=open("countresult","w")
wordslst=[]
#wordsplit=words.split("\t")
dict={}


for item in words:

    wordslst.append(item)
print(wordslst)



for item in wordslst:
    if(item not in dict):
        dict[item]=1
    else:
        dict[item]+=1
print(dict)
for item in dict:
    n= item + str(dict[item])
    out.write(n)




