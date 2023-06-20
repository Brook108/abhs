import networkx as nx
import matplotlib.pyplot as plt

# Define a function to create a call graph
def create_call_graph():

    G = nx.DiGraph()
    G.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
    G.out_degree(1, weight='weight')

    # Add function calls to the graph
    return G


call_graph = create_call_graph()

# Define positions for nodes

# Draw the call graph
nx.draw(call_graph, pos, with_labels=True, node_color='blue', node_size=1000, font_size=12, arrows=True)

# Display the call graph
plt.show()
