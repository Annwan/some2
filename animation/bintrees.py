from dataclasses import dataclass
import networkx as nx

@dataclass
class FB:
    l: object | None
    r: object | None

def allFB(nodes: int ) -> [FB]:
    if nodes % 2 == 0:
        return []
    elif nodes == 1:
        return [FB(None, None)]
    else:
        lst = []
        for i in range(1, nodes, 2):
            for l in allFB(i):
                for r in allFB(nodes - i - 1):
                    lst.append(FB(l, r))
        return lst

def FB2nxGraph(tree: FB, name="X"):
    g = nx.Graph()
    g.add_node(name)
    if (tree.l is not None) and (tree.r is not None):
        l : nx.Graph = FB2nxGraph(tree.l, name+"l")
        r : nx.Graph = FB2nxGraph(tree.r, name+"r")
        g : nx.Graph = nx.union_all([g, l, r])
        g.add_edge(name, name + "l")
        g.add_edge(name, name + "r")
    return g

ALL_13 = [
    FB(l=FB(l=None, r=None),r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=FB(l=None, r=None), r=FB(l=None, r=None))), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)),
    FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=FB(l=None, r=None), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None)), r=FB(l=None, r=None))]
