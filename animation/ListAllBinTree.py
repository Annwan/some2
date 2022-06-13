from manim import *
import networkx as nx
from dataclasses import dataclass

@dataclass
class FBN:
    l: object | None
    r: object | None

def allFBN(nodes: int ) -> [FBN]:
    if nodes % 2 == 0:
        return []
    elif nodes == 1:
        return [FBN(None, None)]
    else:
        lst = []
        for i in range(1, nodes, 2):
            for l in allFBN(i):
                for r in allFBN(nodes - i - 1):
                    lst.append(FBN(l, r))
        return lst

def FBN2nxGraph(tree: FBN, name="Tree"):
    g = nx.Graph()
    g.add_node(name)
    if (tree.l is not None) and (tree.r is not None):
        l : nx.Graph = FBN2nxGraph(tree.l, name+"l")
        r : nx.Graph = FBN2nxGraph(tree.r, name+"r")
        g : nx.Graph = nx.union_all([g, l, r])
        g.add_edge(name, name + "l")
        g.add_edge(name, name + "r")
    return g

class ListAllBinTree(Scene):
    def construct(self):
        g = Graph([], [])
        self.add(g)
        at = []
        for i in range(9):
            print(i)
            for k in allFBN(i):
                at.append(FBN2nxGraph(k))
                
        for l in at:
            gx  = Graph(list(l.nodes), list(l.edges), layout="tree", root_vertex="Tree")
            self.play(Transform(g, gx))
            self.remove(g)
            g = gx
        

