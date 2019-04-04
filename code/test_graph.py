import matplotlib.pyplot as plt
import networkx as nx
G=nx.Graph()

G.add_nodes_from([1,2,3,4,5,6,7,8,9,0],key="A")
# G.add_edges_from([(1,2),(2,3),(3,4),(5,8),(9,1),(2,3),(4,6),(8,2),(7,3)])
G.add_weighted_edges_from([(1,2,1),(2,3,2),(3,4,3),(5,8,4),(9,1,5),(2,3,6),(4,6,7),(8,2,8),(7,3,9)])

print(G.nodes(data=True))

nx.draw(G)
plt.show()