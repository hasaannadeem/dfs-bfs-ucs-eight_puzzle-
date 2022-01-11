#BFS using Queue G1:vertex
from collections import deque
graph={ 'a': set(['b','c']),
        'b': set(['a','d']),
        'c': set(['a','d','f']),
        'd': set(['b','c','e','s']),
        'e': set(['d','h','s','r']),
        'f': set(['G','c','r']),
        'G': set(['f']),
        'h': set(['e','p','q']),
        'p': set(['s','q','h']),
        'q': set(['p','h']),
        'r': set(['e','f']),
        's': set(['d','e','p'])}

#  BFS: Queue 
def bfssearchings(graph, start,goal):
    visited= []
    path=[]
    queue=deque([start])
    
    while queue:
        vertex= queue.popleft()
        
        if vertex not in path:        
           path.extend(vertex)
           visited.extend(vertex)
           queue.extend(list(set(graph[vertex])))
        if goal in path:
            return (path,visited)
        checker=1
        for a in graph:
            for b in graph[a]:
                if b in path:
                    checker=(checker)*(1)
                else:
                     checker=(checker)*(0)
            if(checker>0):
                if a not in visited:
                    visited.extend(a)
    return (path,visited)
p=[]
p.extend(bfssearchings(graph,'s','G'))
print("path :",p[0])
print("visited nodes:",p[1])
