# グラフの表示練習

from graphviz import Digraph


"""
G = Digraph(format="png")
G.attr("node", shape="circle")

N = 15

for i in range(N):
    G.node(str(i), str(i))

for i in range(N):
    if(i - 1) // 2 >= 0:
        G.edge(str((i - 1) // 2), str(i))

G.view()
"""


G = Digraph(format="png")
G.attr("node", shape="square", color="green")
G.attr("edge", color="blue")
G.node("0")
G.node("1")
G.attr("node", shape="star", style="filled", fillcolor="gray85", fontcolor="red")
G.node("2")
G.node("3")
G.attr("node", shape="circle", color="yellow")
G.node("4")

G.edge("0", "1")
G.edge("2", "3")
G.edge("4", "0")
G.edge("4", "2")

G.view()


"""
G = Digraph(format="png")

for i in range(3):
    G.node(str(i), label="state{0}".format(i+1))

edges = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 0]]
edge_labels = ["0.5", "0.5", "0.3", "0.7", "1.0"]

for i, e in enumerate(edges):
    G.edge(str(e[0]), str(e[1]), label=edge_labels[i])

G.view()
"""