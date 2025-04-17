n=input()
k=n.split( )
list=[ ]
con=[]
w=[]
m=0
for i in k:
    list.append(int(i))
for i in list:
    if i>=6:
        con.append(1)
    elif 6>i:
        con.append(0)
print(con)

for j in con:
    if j==1:
        m+=1
        if j == con[-1]:
            w.append(m)
    else:
        w.append(m)
        m=0
print("consistency:",max(w))