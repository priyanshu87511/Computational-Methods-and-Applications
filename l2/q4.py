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


    def oneTwoComponentSizes(self):
        # if there is no edge initially then return 0,0
        if(self.adj == {}):
            return [0,0]
        # taking queue and visited elements
        queue = []
        visited = set()
        keyz = self.adj.keys()
        # taking one component 0 in case we have only one big component
        compo = [0]
        # starting with a node adn implementing bfs
        for node in keyz:
            if(node in visited):
                continue
            cur = 1
            queue.append(node)
            visited.add(node)
            while queue:
                # doing bfs over it
                m = queue.pop(0)
                # appending in the queue only if it is not present in visited 
                for items in self.adj[m]:
                    if items not in visited:
                        cur += 1
                        queue.append(items)
                        visited.add(items)
            compo.append(cur)
        # returnin g top 2 items
        compo = np.sort(compo)
        compo = np.flip(compo)
        return compo[:2]

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

def graph():
    xvalue = []
    yvalue = []
    yvalue2 = []
    # taking elements in range 0.01 on gap of 10^-4
    pval = np.arange(0, 0.01, 0.0002)
    for p in pval:
        # appending value in xvalue
        print(p)
        xvalue.append(p)
        yval = 0
        yval1 = 0
        # taking each case 50 times
        for it in range (0, 50):
            # taking a graph with the probability and checking if it is connected
            g = ERRandomGraph(1000)
            g.sample(p)
            val = g.oneTwoComponentSizes()
            yval += val[0]/50
            yval1 += val[1]/50
        yvalue.append(yval/1000)
        yvalue2.append(yval1/1000)
    # plotting the graph
    plt.plot(xvalue, yvalue, c="green", label = "Largest connected component")
    plt.plot(xvalue, yvalue2, c="blue", label = "2nd largest connected component")
    threshold = 0.01
    yvalue = np.flip(yvalue)
    xvalue = np.flip(xvalue)
    for it in range(len(yvalue)):
        if(yvalue[it]<0.999):
            threshold = xvalue[it]
            break
    plt.axvline(x=0.001, c="red", label="Largest CC size threshold")
    plt.axvline(x=threshold, c="yellow", label="Connectedness Threshold")
    plt.xlabel("p")
    plt.ylabel("fraction of nodes")
    plt.title("Fraction of nodes in the largest and second-largestconnected components (CC) of G(1000, p) as function of p")
    plt.legend()
    plt.grid(True)
    plt.savefig("q4.png")
    plt.show()

# test in
# g = UndirectedGraph(6)
# g = g + (1, 2)
# g = g + (3, 4)
# g = g + (6, 4)
# print(g.oneTwoComponentSizes())
graph()