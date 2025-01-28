G={
        '5':['2','7'],
        '2':['3','4'],
        '7':['8'],
        '2':[],
        '4':['8'],
        '8':[]
        }
V=[]
q=[]
def bfs(V,G,N):
         V.append(N)
         q.append(N)
         while q:
             m=q.pop(0)
             print (m,end=" ")
             for neighbour in G[m]:
                  V.append(neighbour)
                  q.append(neighbour)

print("it is the depth first search")
bfs(V,G,'5')
         