import project
G=project.Graph()
G.addVertex(project.Position(0,0,0))
G.addVertex(project.Position(1,1,1))
G.addVertex(project.Position(2,2,2))
G.addEdge(project.Position(0,0,0),project.Position(1,1,1))
G.addEdge(project.Position(0,0,0),project.Position(2,2,2))
G.addEdge(project.Position(1,1,1),project.Position(2,2,2))
G.addEdge(project.Position(1,1,1),project.Position(0,0,0))
G.addEdge(project.Position(2,2,2),project.Position(0,0,0))
G.addEdge(project.Position(2,2,2),project.Position(1,1,1))

def test_left():
    assert project.left(G.contain)==3
    assert project.left((project.Position(3,0,3),project.Position(5,0,2)))==2
    p1=project.Position(1,1,0)
    p2=project.Position(4,2,5)
    p2.isThere==True
    assert project.left((p1,p2))==1

def test_minPop():
    assert project.minPop(G.contain)==project.Position(0,0,0)
    assert project.minPop((project.Position(3,0,3),project.Position(5,0,2)))==project.Position(3,0,3)
    p1=project.Position(1,1,0)
    p2=project.Position(4,2,5)
    p2.isThere==True
    assert project.minPop((p1,p2))==project.Position(1,1,0)

def test_indexOfVertex():
    assert project.indexOfVertex(G,0,0)==0
    assert project.indexOfVertex(G,1,1)==1
    assert project.indexOfVertex(G,5,6)==-1









