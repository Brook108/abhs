from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput


def Run():
    print("Function B")

def ReqOrderInsert():
    Run()

graphviz = GraphvizOutput(output_file='call_graph.png')
with PyCallGraph(output=graphviz):
    ReqOrderInsert()
