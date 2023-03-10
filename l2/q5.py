# importing libraries
import matplotlib.pyplot as plt
import networkx as nx
import random

# in class lattice
class Lattice:
    # defining init fucntion for taking the node list and edge list and initialising edge colors
    def __init__(self, n = 10):
        self.n = n
        self.graph = nx.grid_2d_graph(n, n)
        self.nodePos = {} 
        self.edgeList = []
        self.edge_colors = 'r'
        for x, y in self.graph.nodes():
            self.nodePos[(x, y)] = (x, y)
    
    # show function is created to display nodes and then edges and saving the plot
    def show(self):
        nx.draw_networkx_nodes(G=self.graph, pos=self.nodePos, node_size=0)
        nx.draw_networkx_edges(G=self.graph, pos=self.nodePos, edgelist=self.edgeList, edge_color=self.edge_colors)
        plt.savefig("q5.png")
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
        height_lst = []
        # for each x
        for x in range(self.n):
            visited = set()
            queue = []
            height = self.n - 1
            queue.append((x, self.n - 1))
            visited.add((x, self.n - 1))
            # doing bfs
            while(queue):
                m = queue.pop(0)
                visited.add(m)
                if m in self.edge.keys():
                    for ele in self.edge[m]:
                        if(ele not in visited):
                            height = min(height, ele[1])
                            visited.add(ele)
                            queue.append(ele)
                # if we reached bottom layer
                if(m[1] == 0):
                    break
            # maintaining height list of each node how down it can come
            height_lst.append(height)
        self.height = height_lst
        # returning if we got a path
        for items in visited:
            if(items[1] == 0):
                return True
        return False
    
    def showPaths(self):
        # using one instance of existstopdownpath for creation of self.height
        run_once = self.existsTopDownPath()
        # colours in the box
        options = ['r', 'g']
        colour_ed = set()
        pred_map = {}
        self.edge_colors = []
        # making the initial colours set
        for edge in self.edgeList:
            self.edge_colors.append(options[0])
        # for all x
        for x in range(self.n):
            visited = set()
            queue = []
            queue.append((x, self.n - 1))
            visited.add((x, self.n - 1))
            flag = 1
            # doing bfs
            while(queue and flag):
                m = queue.pop(0)
                visited.add(m)
                if m in self.edge.keys():
                    for ele in self.edge[m]:
                        if(ele not in visited):
                            visited.add(ele)
                            pred_map[ele] = m
                            queue.append(ele)
                        if(ele[1] == self.height[x]):
                            flag = 0
                            break
            # change color of all which have the shortest and deep path and tracing the path
            for items in visited:
                if(items[1] == self.height[x]):
                    path = []
                    while(pred_map.get(items) and items != (x, self.n - 1)):
                        colour_ed.add((items, pred_map[items]))
                        colour_ed.add((pred_map[items], items))
                        path.append((items, pred_map[items]))
                        items = pred_map[items]
                    break
        it = 0
        # giving color green
        for edge in self.edgeList:
            if edge in colour_ed:
                self.edge_colors[it] = options[1]
            it += 1


l = Lattice(100)
l.percolate(0.8)
print(l.existsTopDownPath())
l.showPaths()
l.show()