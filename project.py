import sys

class Position:
    def __init__(self, value, lenght, width):
        self.value=value
        self.lenght=lenght
        self.width=width
        self.isThere=False
        self.wayHelp=None

class Graph:
    def __init__(self) -> None:
        self.contain=list()
        self.neighboursList=list()

    def addVertex(self,Position):
        self.contain.append(Position)
        self.neighboursList.append(list())
    def addEdge(self, From ,To):
        indexFrom=self.contain.index(From)
        #indexTo=self.contain.index(To)
        self.neighboursList[indexFrom].append(To)

    def IsEdgeBetween(self, From, To):
        indexFrom=self.contain.index(From)
        indexTo=self.contain.index(To)
        return self.contain[indexTo] in self.neighboursList[indexFrom]
    def neighbours(self, Vertex):
        index=self.contain.index(Vertex)
        return self.neighboursList[index]
    
class Map:
    def __init__(self) -> None:
        self.map=[[]]
        
    def load(self, fajlName):
        with open(fajlName, "r") as f:
            sorok = f.readlines()
            tomb = []
            for sor in sorok:
                sor = sor.strip()
                szamok = [int(x) for x in sor]
                tomb.append(szamok)
            
        self.map=tomb

    def printTheMap(self,table):
        for i in table:
            for j in i:

                if j == -1:
                
                    sys.stdout.write("\x1b[40m  \x1b[0m") 
                elif j == 1:
                    
                    sys.stdout.write("\x1b[47m  \x1b[0m")  
                elif j == 2:
                    
                    sys.stdout.write("\x1b[46m  \x1b[0m")  
                elif j == 3:
                    
                    sys.stdout.write("\x1b[42m  \x1b[0m")  
                elif j == 4:
                    
                    sys.stdout.write("\x1b[43m  \x1b[0m")  
                elif j == 5:
                    
                    sys.stdout.write("\x1b[41m  \x1b[0m")  
                elif j == 6:
                    
                    sys.stdout.write("\x1b[45m  \x1b[0m")  
                else:
                    
                    sys.stdout.write("\x1b[44m  \x1b[0m")  
            print()
        sys.stdout.write("\x1b[0m\n")  


def indexOfVertex(G,l,w):
    counter=0
    for i in range(len(G.contain)):
        if G.contain[i].lenght==l and G.contain[i].width==w:
            return counter
        counter+=1
        
    return -1
    
def minPop(L):
    min=0
    helper=list()
    for i in range(len(L)):
        if L[i].isThere==False:
            helper.append(L[i])
        
    for i in range(len(helper)):
        if helper[i].value<helper[min].value:
            min=i
        
    return helper[min]
    
def left(L):
    db=0
    for i in range(len(L)):
        if L[i].isThere==False:
            db+=1

    return db
    
def dijkstraResult(G, l,w):
    d=list()
    s=list()
    for i in range(len(G.neighboursList)):
        x=G.contain[i]
        d.append(Position(sys.maxsize,G.contain[i].lenght,G.contain[i].width))
        s.append(x)

    d[indexOfVertex(G,l,w)].value=0
    leftItemsCount=left(d)
    while leftItemsCount!=0:
        u=minPop(d)
        d[indexOfVertex(G,u.lenght,u.width)].isThere=True
        helperList=G.neighbours(s[indexOfVertex(G,u.lenght,u.width)])
        for i in range(len(helperList)):
            helper=indexOfVertex(G,helperList[i].lenght,helperList[i].width)
            if d[indexOfVertex(G,u.lenght,u.width)].value+helperList[i].value<d[helper].value:
                d[helper].value=d[indexOfVertex(G,u.lenght,u.width)].value+helperList[i].value
                s[helper].value=d[indexOfVertex(G,u.lenght,u.width)].value+helperList[i].value
                d[helper].wayHelp=u
        leftItemsCount=left(d)
    return d



def main():
    m=Map()
    m.load("map.txt")
    matrix=m.map
    g=Graph()
    m.printTheMap(matrix)
    l=0
    for i in matrix:
        w=0
        for j in i:
            if j<=4:
                g.addVertex(Position(j,l,w))
            w+=1
        l+=1
    
    counter=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]<=4:
                if i-1>=0 and matrix[i-1][j]<=4:
                    new=Position(matrix[i-1][j],i-1,j)
                    g.addEdge(g.contain[counter],new)
                if j-1>=0 and matrix[i][j-1]<=4:
                    new=Position(matrix[i][j-1],i,j-1)
                    g.addEdge(g.contain[counter],new)
                if i+1<len(matrix) and matrix[i+1][j]<=4:
                    new=Position(matrix[i+1][j],i+1,j)
                    g.addEdge(g.contain[counter],new)
                if j+1<len(matrix[i]) and matrix[i][j+1]<=4:
                    new=Position(matrix[i][j+1],i,j+1)
                    g.addEdge(g.contain[counter],new)
                counter+=1
    startLenght=int(input(f"Start Lenght coordinate (0-{len(matrix)-1}): "))
    startWidth=int(input(f"Start Width coordinate (0-{len(matrix[0])-1}): "))
    stopLenght=int(input(f"Stop Lenght coordinate (0-{len(matrix)-1}): "))
    stopWidth=int(input(f"Stop Width coordinate (0-{len(matrix[0])-1}): "))
    if matrix[startLenght][startWidth]>=5 or matrix[stopLenght][startWidth]>=5:
        sys.exit("This location is not accessible")
    L=dijkstraResult(g,startLenght,startWidth)
    coordinateLenght=list()
    coordinateWidth=list()
    for i in range(len(L)):
        if stopLenght==L[i].lenght and stopWidth==L[i].width:
            helper=False
            poz=L[i]
            while helper!=True:
                if poz.wayHelp!=None:
                    coordinateLenght.append(poz.lenght)
                    coordinateWidth.append(poz.width)
                    
                    matrix[poz.lenght][poz.width]=-1
                else:
                    coordinateLenght.append(poz.lenght)
                    coordinateWidth.append(poz.width)
                    
                    matrix[poz.lenght][poz.width]=-1
                    helper=True
                poz=poz.wayHelp

    coordinateLenght.reverse()
    coordinateWidth.reverse()
    for i in range(len(coordinateWidth)):
        print(f"Coordinate: {coordinateLenght[i]} : {coordinateWidth[i]}")
    m.printTheMap(matrix)

    
        
main()

