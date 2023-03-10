# importing library for plotting the graph
import matplotlib.pyplot as plt

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
        plt.scatter(xvalues, yvalues, c="blue", label="Actual Degree Distribution")
        plt.axvline(x=sum, c="red", label="Avg. Node Degree")
        plt.xlabel("Node Degree")
        plt.ylabel("Fraction of Nodes")
        plt.title("Node Degree Distribution")
        plt.legend()
        plt.grid(True)
        plt.savefig("q1.png")
        plt.show()


# taking the testcase
g = UndirectedGraph()
g = g + 100
g = g + (1, 2)
g = g + (1, 100)
g = g + (100, 3)
g = g + 20
g.plotDegDist()