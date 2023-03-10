# importing libraries
import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np

class Lattice:
    # initialising all nodes and edges along with colour
    def __init__(self, n = 10):
        self.n = n
        self.graph = nx.grid_2d_graph(n, n)
        self.nodePos = {} 
        self.edgeList = []
        for x, y in self.graph.nodes():
            self.nodePos[(x, y)] = (x, y)
    
    # showing the graph and saving the figure
    def show(self):
        nx.draw_networkx_nodes(G=self.graph, pos=self.nodePos, node_size=1)
        nx.draw_networkx_edges(G=self.graph, pos=self.nodePos, edgelist=self.edgeList, edge_color=self.edge_colors)
        plt.savefig("q6.png")
        plt.show()

    # making edges with given probabilities
    def percolate(self, prob = 0.2):
        # for all y we are checking if horizontal lines are made
        for y in range(self.n):
            for x in range(self.n - 1):
                rand = random.random()
                if(rand < prob):
                    self.edgeList.append(((x,y),(x+1,y)))
                    self.edgeList.append(((x+1,y),(x,y)))
        # lines vertical
        for x in range(self.n):
            for y in range(self.n - 1):
                rand = random.random()
                if(rand < prob):
                    self.edgeList.append(((x,y),(x,y+1)))
                    self.edgeList.append(((x,y+1),(x,y)))
        # adjacency list of lattice
        map_edges = {}
        for edge in self.edgeList:
            if(edge[1] in map_edges.keys()):
                map_edges[edge[1]].add(edge[0])
            else:
                map_edges[edge[1]]=set()
                map_edges[edge[1]].add(edge[0])
            if(edge[0] in map_edges.keys()):
                map_edges[edge[0]].add(edge[1])
            else:
                map_edges[edge[0]]=set()
                map_edges[edge[0]].add(edge[1])
        self.edge = map_edges
        # converting the values in list form
        for key in self.edge.keys():
            self.edge[key] = list(self.edge[key])

    # checking if a path exists from top to bottom
    def existsTopDownPath(self):
        visited = set()
        queue = []
        # for each x taking nodes at once
        for x in range(self.n):
            queue.append((x, self.n - 1))
            visited.add((x, self.n - 1))
        # taking them as starting nodes doing bfs
        while(queue):
            m = queue.pop(0)
            visited.add(m)
            if m in self.edge.keys():
                for ele in self.edge[m]:
                    if(ele not in visited):
                        visited.add(ele)
                        queue.append(ele)
                # if we reached bottom then we stop
                if(m[1] == 0):
                    break
        # checking if we reached
        for items in visited:
            if(items[1] == 0):
                return True
        return False


# creating a function to display g
def graph():
    xvalues = []
    yvalues = []
    # for all probabilities
    probs = np.arange(0,1.01,0.01)
    for prob in probs:
        print(prob)
        xvalues.append(prob)
        yval = 0
        # for these iteration averaging the values
        for it in range(0,50,1):
            # creating lattice for verification
            l = Lattice(100)
            l.percolate(prob)
            if(l.existsTopDownPath()):
                yval += 1
        yvalues.append(yval/50)
    # plotting the graph
    plt.plot(xvalues, yvalues, c="blue")
    plt.xlabel("p")
    plt.ylabel("Fraction of runs end-to-end percolation occurred")
    plt.title("Critical cut-off in 2-D bond percolation")
    plt.legend()
    plt.grid(True)
    # saving the graph
    plt.savefig("q6.png")
    plt.show()


# test inn
graph()