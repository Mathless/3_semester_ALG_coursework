from graphviz import Digraph
def visualize_tree(tree):
    if tree.val == None: return
    def add_nodes_edges(tree, dot=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree), label=str(tree.val), fillcolor=tree.color, style="filled", fontcolor = "white")

        # Add nodes
        if tree.left.val != None:
            dot.node(name=str(tree.left), label=str(tree.left.val), fillcolor=tree.left.color, style="filled", fontcolor = "white")
            dot.edge(str(tree), str(tree.left))
            dot = add_nodes_edges(tree.left, dot=dot)

        if tree.right.val is not None:
            dot.node(name=str(tree.right), label=str(tree.right.val), fillcolor=tree.right.color, style="filled", fontcolor = "white")
            dot.edge(str(tree), str(tree.right))
            dot = add_nodes_edges(tree.right, dot=dot)

        return dot

    # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(tree)

    return dot


def show(tree):
    dot = visualize_tree(tree.root)
    dot.format = 'png'
    dot.view(filename='digraph', directory='./')