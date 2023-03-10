# importing library for plotting the graph
import matplotlib.pyplot as plt
import random as rand
import math
import numpy as np

# defining the class
class UndirectedGraph:
    # making sure if no argument is passed or one is passed
    def __init__(self, n = None):
        # if argument is passed
        if(n!=None):
            # initiate a empty list to every node
            adj_list = {}
            for node in range (n):
                adj_list[node+1] = []
            self.adj = adj_list
        # if it is already free
        else:
            self.adj = {}
        # saving the initial number of NODES
        self.ini_node = n

    # for adding any node to the  graph
    def addNode (self, add):
        # if we declared the number of nodes before then we cant add any new node
        if(self.ini_node != None):
            if(self.ini_node < add):
                raise Exception("Node index cannot exceed number of nodes")
        # otherwise adding the vertex if it is already not there
        elif(not self.adj.get(add)):
            self.adj[add] = []

    # function for adding the edge 
    def addEdge (self, node1, node2):
        # if node1 is not present we add it and similar for other
        if(not self.adj.get(node1)):
            self.adj[node1] = []
        if(not self.adj.get(node2)):
            self.adj[node2] = []
        # adding the edge in both of them
        self.adj[node1].append(node2)
        self.adj[node2].append(node1)

    # overloading the add operator
    def __add__(self, node):
        # if node is added then calling that function
        if(type(node)==int):
            self.addNode(node)
        # otherwise calling the add edge function
        elif(type(node)==tuple):
            self.addEdge(node[0], node[1])
        # for any other input raise exception
        else:
            raise Exception("Unexpected Input")
        return self

    # print function
    def __str__(self):
        # initialising the number of keys and values and adding for each instance
        keys = 0
        values = 0
        for key in self.adj:
            keys += 1
            values += len(self.adj[key])
        # printing the first line
        strr = "Graph with " + str(keys) + " nodes and " + str(int(values/2)) + " edges. Neighbours of the nodes are belows:\n"
        # for every key in our dictionary we are appending neighbour print statement
        for key in self.adj:
            strr += "Node " + str(key) + ": " + str(list(set(self.adj[key]))) + "\n"
        return strr

    # function to plot
    def plotDegDist(self):
        # initialisting xvalues with yvalues
        yvalues = []
        xvalues = []
        sum = 0
        for val in range(len(self.adj)):
            # for every val initialising the lists
            xvalues.append(val)
            yvalues.append(0)
        #for every key increasing the deg by 1
        for key in self.adj:
            yvalues[len(self.adj[key])]+=1
        # adjusting the values and making them suitable for graph
        for val in range(len(self.adj)):
            yvalues[val]=yvalues[val]/len(self.adj)
            sum += xvalues[val]*yvalues[val]
        # plotting the graph with the values and line associated with average degree
        plt.scatter(xvalues, yvalues, c="blue", label="Actual Degree Distribution", marker=".")
        plt.axvline(x=sum, c="red", label="Avg. Node Degree")
        plt.xlabel("Node Degree")
        plt.ylabel("Fraction of Nodes")
        plt.title("Node Degree Distribution")
        plt.legend()
        plt.grid(True)
        plt.savefig("q2.png")
        plt.show()

    # creating the isconnected function
    def isConnected(self):
        # if adj is already empty means we don't have any vertex so considering graph to be connected
        if(self.adj == {}):
            return True
        # taking queue and visited elements
        queue = []
        visited = set()
        keyz = self.adj.keys()
        node = list(keyz)[0]
        queue.append(node)
        # starting with a node
        while queue:
            # doing bfs over it
            m = queue.pop(0)
            visited.add(m)
            # appending in the queue only if it is not present in visited 
            for items in self.adj[m]:
                if items not in visited:
                    queue.append(items)
        # if all elements are visited then it returns true
        if(len(visited)==len(self.adj)):
            return True
        # false
        else:
            return False

    
# derived class for er graphs
class ERRandomGraph(UndirectedGraph):
    # sample function to take care of probability
    def sample(self, pro):
        # iterating in double loop to make the edge in case of probability satisfied
        keyz = self.adj.keys()
        keys = list(keyz)
        for i in range (len(keyz)):
            for j in range (i+1, len(keyz)):
                randm = rand.random()
                # check
                if(randm < pro):
                    self.adj[keys[i]].append(keys[j])
                    self.adj[keys[j]].append(keys[i])

# creating the graph function
def graph():
    # initialising xvalue and yvalue
    xvalue = []
    yvalue = []
    # taking elements in range 0.1 on gap of 2(10^-3
    pval = np.arange(0, 0.1001, 0.002)
    for p in pval:
        # appending value in xvalue
        xvalue.append(p)
        yval = 0
        # taking each case 1000 times
        for it in range (0, 1000):
            # taking a graph with the probability and checking if it is connected
            g = ERRandomGraph(100)
            g.sample(p)
            if(g.isConnected()):
                yval+=1
        yvalue.append(yval/1000)
    # plotting the graph
    plt.plot(xvalue, yvalue, c="blue")
    plt.axvline(x=math.log(100, math.e)/100, c="red", label="Theoritical Threshold")
    plt.xlabel("p")
    plt.ylabel("fraction of runs G(100, p) is connected")
    plt.title("Connectedness of a G(100, p) as function of p")
    plt.legend()
    plt.grid(True)
    plt.savefig("q3.png")
    plt.show()

# test in
graph()