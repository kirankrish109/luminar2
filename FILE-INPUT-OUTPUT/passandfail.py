std=open("students","r")
fail=open("failedstd","r")
passs=open("passstd","w")

st=set()
failst=set()


for data in std:
        st.add(data)

for data in fail:
        failst.add(data)

passst=st-failst

for item in passst:
    passs.write(item)
