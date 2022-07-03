"""
Implementation of BFS algorithm
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
    
    def bfsUtil(self,visited,vertex):
        queue=[]
        queue.append(vertex)
        visited[vertex]=True

        while(queue):
            frontNode=queue[0]
            queue.remove(frontNode)
            print(frontNode,end=" ")

            for neighbour in self.adjList[frontNode]:
                if(not visited[neighbour]):
                    queue.append(neighbour)
                    visited[neighbour]=True
    

    def bfs(self):
        visited={}
        for vertex in self.adjList:
            visited[vertex]=False 
        for vertex in self.adjList:
            if(not visited[vertex]):
                self.bfsUtil(visited,vertex)



    def printAdjList(self):
        for vertex in self.adjList:
            print(vertex,"->",end=" ")
            for neighbour in self.adjList[vertex]:
                print(neighbour,end=",")
            
            print()


if __name__=="__main__":

    graph=Graph(5)
    graph.addEdges(0,1)
    graph.addEdges(1,2)
    graph.addEdges(2,3)
    graph.addEdges(3,4)
    
    graph.bfs()    #0 1 2 3 4

    print()

    graph1=Graph(4)
    graph1.addEdges(0, 1)
    graph1.addEdges(0, 2)
    graph1.addEdges(1, 2)
    graph1.addEdges(2, 3)

    graph1.bfs()


    