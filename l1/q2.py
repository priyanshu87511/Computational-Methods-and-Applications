import matplotlib.pyplot as plt
import random as rand

# creating the class dice
class Dice:
    
    # creating dice of the given number of faces
    def __init__ (self, faces = 6):
        # if faces are less than 4 or of any other datatype than int then raising exception
        if not isinstance(faces, int) or (faces < 4):
            raise Exception("Cannot construct the dice")
        # otherwise saving the number of faces
        else:
            self.faces = faces

    # taking probabilities of every face
    def setProb (self, prob):
        # if probabilities of all faces is not given or if the sum is not 1 then throw exception
        if (len(prob) != self.faces) or (sum(prob) != 1):
            raise Exception("Invalid probability distribution")
        # otherwise saving the probability
        else:
            self.prob = prob

    # overloading the print function and printing the faces with probabilities
    def __str__(self):
        return "Dice with " + str(self.faces) + " faces and probability distribution " + str(self.prob)
    
    # rolling the dice given number of times and plotting the graph 
    def roll (self, rolling):
        # creating faces and values list to store actual probabilities
        faces = []
        values = []
        current = 0
        # for each face setting probability to 0 initially
        for prob in self.prob:
            current += 1
            values.append(0)
            faces.append(current)
        # rolling the dice given number of times
        for roll in range (rolling):
            current = 0
            # taking random value between 0 and 1
            valu = rand.random()
            prob_now = 0
            # taking where we got the value and choosing appropriate face and output of the exp
            for prob in self.prob:
                prob_now += prob
                if(prob_now > valu):
                    values[current] += 1
                    break
                current += 1
        # plotting the graph with expected value
        self.prob = list(self.prob)
        for i in range(self.faces):
            self.prob[i] = self.prob[i] * rolling
        plt.bar(faces, self.prob, width=0.25, label = "expected")
        # making suitable adjustments for actual values and plotting the graph
        for i in range(self.faces):
            faces[i] = faces[i] + 0.25
        # making the graph
        plt.bar(faces , values , width=0.25, label = "actual")
        plt.xlabel("Faces")
        plt.ylabel("Occurance")
        plt.title("Outcomes")
        plt.legend()
        plt.savefig("q2.png")
        # showing the graph
        plt.show()

# testing for test case
d = Dice(5)
print(d.faces)
d.setProb((0.25, 0.25, 0.25, 0.10, 0.15))
print(d.prob)
print(d)
d.roll(100)