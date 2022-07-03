"""
Implementation of DFS Algorithm
"""

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.adjList={}
    
    def addEdges(self,src,dest,direction=0):
        #direction=0 => undirected graph
        #direction=1 => directed graph

        #Adding an edge from src to dest
        if(src not in self.adjList):
            self.adjList[src]=[dest]
        else:
            self.adjList[src].append(dest)
        
        if(direction==0):
            if(dest not in self.adjList):
                self.adjList[dest]=[src]
            else:
                self.adjList[dest].append(src)
    
    def dfsUtil(self,visited,vertex):
        visited[vertex]=True
        print(vertex, end=" ")

        for neighbour in self.adjList[vertex]:
            if(not visited[neighbour]):
                self.dfsUtil(visited,neighbour)
    def dfs(self):
        visited={}

        for vertex in self.adjList:
            visited[vertex]=False
        
        for vertex in self.adjList:
            if(not visited[vertex]):
                self.dfsUtil(visited,vertex)

    def printAdjList(self):
        for vertex in self.adjList:
            print(vertex,"->",end=" ")
            for neighbour in self.adjList[vertex]:
                print(neighbour,end=",")
            
            print()


if __name__=="__main__":

    graph=Graph(5)
    graph.addEdges(0,1)
    graph.addEdges(1,3)
    graph.addEdges(2,3)
    graph.addEdges(3,4)
    
    graph.dfs()   #0 1 3 2 4

    print()

    graph1=Graph(4)
    graph1.addEdges(0, 1)
    graph1.addEdges(1, 3)
    graph1.addEdges(1, 2)
    graph1.addEdges(2, 3)

    graph1.dfs()        #0 1 3 2