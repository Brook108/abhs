import networkx as nx

def convert_to_tree(graph_text):
    # Create an empty directed graph
    tree = nx.DiGraph()

    # Add edges to the graph
    for parent, children in graph_text.items():
        tree.add_edges_from([(parent, child) for child in children])

    # Find the root node of the tree
    roots = [node for node in tree.nodes if tree.in_degree(node) == 0]

    # Select the first root as the main root (assuming there's only one root)
    root = roots[0]

    # Create a depth-first search tree starting from the main root
    dfs_tree = nx.dfs_tree(tree, root)

    return dfs_tree

def preorder_traversal(tree, node):
    print(node)
    for child in tree.successors(node):
        preorder_traversal(tree, child)

# Example graph_text
graph_text = {
    'N_2282': ['N_2418'],
    'N_2418': ['N_2859', 'N_3037', 'N_2762', 'N_3038', 'N_2763', 'N_2788', 'N_458', 'N_3039', 'N_2764', 'N_3043', 'N_2765', 'N_2397', 'N_2766', 'N_3053', 'N_2767', 'N_3055', 'N_2768', 'N_3048', 'N_2769', 'N_3051', 'N_2770', 'N_2789', 'N_459', 'N_456', 'N_3052', 'N_2771', 'N_3056', 'N_2773', 'N_3059', 'N_2783', 'N_3072', 'N_2779', 'N_3064', 'N_2772', 'N_3062', 'N_2786'],
    'N_3038': ['N_1138', 'N_1084', 'N_42', 'N_1130'],
    'N_2788': ['N_1435', 'N_1050', 'N_1446', 'N_214'],
    'N_3039': ['N_3040', 'N_3041'],
    'N_2764': ['N_39', 'N_23', 'N_24', 'N_18', 'N_19', 'N_214', 'N_20', 'N_22', 'N_25'],
    'N_3043': ['N_213'],
    'N_2765': ['N_14', 'N_5']
}
print(graph_text)

# Convert graph_text to a tree structure
tree = convert_to_tree(graph_text)

# Perform preorder traversal starting from the root
root = [node for node in tree.nodes if tree.in_degree(node) == 0][0]
preorder_traversal(tree, root)

