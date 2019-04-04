import matplotlib.pyplot as plt
import networkx as nx
G=nx.Graph()

# G.add_nodes_from([1,2,3,4,5,6,7,8,9,0],key="A")
# # G.add_edges_from([(1,2),(2,3),(3,4),(5,8),(9,1),(2,3),(4,6),(8,2),(7,3)])
# G.add_weighted_edges_from([(1,2,1),(2,3,2),(3,4,3),(5,8,4),(9,1,5),(2,3,6),(4,6,7),(8,2,8),(7,3,9)])

# keyboard_config  =   [
#                         ('1','2','3','4','5','6','7','8','9','0'),
#                         ('q','w','e','r','t','y','u','i','o','p'),
#                         ('a','s','d','f','g','h','j','k','l'),
#                         ('z','x','c','v','b','n','m'),
#                         ('\t\tspace\t\t','backspace','enter','save')
#                     ]

keyboard_config  =   [
                        ('1','2','3'),
                        ('q','w','e'),
                        ('a','s','d'),
                    ]


for t_ in range(len(keyboard_config)):
    G.add_nodes_from(list(t))
    for i in range(0,len(t)):
        e=[(t[i],t[i+1],1) for i in range(0,len(t)-1)]
    e.append((t[0],t[len(t)-1],1))
    G.add_weighted_edges_from(e)

    for i in range(0,len(t)):


print(G.nodes(data=True))
nx.draw(G)
plt.show()