"""
Implementation Using Adjacency List
"""

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.edges={}
    
    def addEdges(self,src,dest,direction=0):
        #direction=0 => undirected graph
        #direction=1 => directed graph

        #Adding an edge from src to dest
        if(src not in self.edges):
            self.edges[src]=[dest]
        else:
            self.edges[src].append(dest)
        
        if(direction==0):
            if(dest not in self.edges):
                self.edges[dest]=[src]
            else:
                self.edges[dest].append(src)
    
    
    def printAdjList(self):
        for vertex in self.edges:
            print(vertex,"->",end=" ")
            for neighbour in self.edges[vertex]:
                print(neighbour,end=",")
            
            print()
    

if __name__=="__main__":

    #Creating an Undirected Graph
    graph=Graph(5)
    graph.addEdges(0,1)
    graph.addEdges(1,2)
    graph.addEdges(2,3)
    graph.addEdges(3,4)

    graph.printAdjList() 

    #Creating a Directed Graph
    graph1=Graph(5)
    graph1.addEdges(0,1,1)
    graph1.addEdges(1,2,1)
    graph1.addEdges(2,3,1)
    graph1.addEdges(3,4,1)

    graph1.printAdjList()






    



