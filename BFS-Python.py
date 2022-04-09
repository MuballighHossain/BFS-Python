# ====== ====== ====== QUESTION 2 ====== ======  ======
graph_2=[]
with open("Question2 input1.txt",'r') as f:
    lines = f.readlines()[2:]
for line in lines:
    graph_2.append(line.split())    
rows = len(graph_2)
cols = len(graph_2[0])
def tester(graph_2):
    vistList = set()
    levels = 1 #Level 1
    def bfs(r,c,visitList):
        q = collections.deque()
        vistList.add((r,c))
        q.append((r,c))
        while q:
            rows,cols =q.popleft()
            neighborTraversal=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in neighborTraversal:
                r = rows+dr
                c = cols+dc
                if (
                        (r) in range(rows) and 
                        (c) in range(cols) and  
                        graph_2[r][c]=='H' and            
                        (r,c) not in vistList
                    ):
                        q.append((r,c))
                        vistList.add((r,c))
                        graph_2[r][c]='A'  
                        
    for r in range(rows):
        for c in range(cols):
            if graph_2[r][c] == 'A' and (r,c) not in vistList:
                levels += 1 
                bfs(r,c,vistList) 
    return levels
value = tester(graph_2)
print("\nQuestion 2 Output")
print("Time : ", value) 
