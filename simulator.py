import random
"""
maxnodes = 4
experiments =2
runsPerExp = 10
roundsPerRun = 10
maxnodeval = 200
"""

nodes = []


def dumpstates():
    """ Prints the nodes representation."""
    string = ""
    for i in range(len(nodes)):
        print("----Node[%d].my_val=%d;" % (i,nodes[i].value))
        

def readvalues(filename):
    """reads input configuration from filename"""
    file = open(filename,"r")
    for line in file:
        results = line[:-1].split(",")
        results = tuple([int(elem) for elem in results])
    return results

def selectRandomInt(maxvalue):
    """ Selects a random value between 0 and (maxvalue-1)."""
    return int(random.random()*maxvalue)

def selectRandomNode():
    """ Selects a random node by returning it's index."""
    return selectRandomInt(maxnodes)

def initnodes(algorithm):
    """ Initializes the nodes given an algorithm."""
    return algorithm.execute()

def getmax(i,j):
    """ Returns the maximum value of i and j."""
    return (i,j)[i<j] # true - 1; false - 0

def assertAlgo(maxInNetwork):
    """Verifies the value of the nodes to equal maxInNetwork. 0-incorrect.1-correct."""
    if (maxInNetwork>0):
        for node in nodes:
            if (node.value != maxInNetwork):
                return 0
        return 1
    return 0

def encounter( i, j):
    """Specifies the algorithm to use when two nodes collide."""
    nodes[i].value = getmax(nodes[i].value, nodes[j].value)


class ErrorAlgorithm(Exception):
    """Error to be used for abstract classes."""
    def __str__(self):
        return "Please implement all the methods."

class Node:
    """Class node defines an agent."""
    def __init__(self):
        self.value = selectRandomInt(maxnodeval)
    
    def setValue(self, val):
        self.value = val

class InitAlgorithm:
    """Abstract class of initializors"""
    def execute(self):
        raise ErrorAlgorithm
    
class AllNodesEqual(InitAlgorithm):
    """Initializes all agents with the same value"""
    def __init__(self):
        super(AllNodesEqual, self)
    
    def execute(self):
        maxInNetwork = selectRandomInt(maxnodeval)
        for node in nodes:
            node.setValue(maxInNetwork)
        return maxInNetwork
    
    def __str__(self):
        return "all nodes equal"

class AllNodesDif(InitAlgorithm):
    """Initializes all agents with different values from 0 to maxnodeval"""
    def __init__(self):
        super(AllNodesDif, self)
    
    def execute(self):
        maxInNetwork = -1
        for node in nodes:
            randomVal = selectRandomInt(maxnodeval)
            maxInNetwork = getmax(maxInNetwork, randomVal)
            node.value = randomVal
        return maxInNetwork
    
    def __str__(self):
        return "all nodes different"
    

# MAIN #


def main():
    
    random.seed() # initializes the seed with the current system time (default)
    global nodes 
    global maxnodes
    global experiments
    global runsPerExp
    global roundsPerRun
    global maxnodeval
    maxnodes, experiments, runsPerExp, roundsPerRun, maxnodeval = readvalues("specifications.txt")
    
    for i in range(maxnodes):
        nodes += [Node()]
        
    print("STARTING %d experiments, %d runs each\n" % (experiments, runsPerExp))
    
    exps = [AllNodesEqual(), AllNodesDif()]
    
    for experiment in range(experiments):
        for run in range(runsPerExp):
            maxInNetwork = initnodes(exps[experiment])
            
            for round in range(roundsPerRun):
                i = selectRandomNode()
                j = selectRandomNode()
                encounter(i,j)
            if (assertAlgo(maxInNetwork)):
                print("\n--Experiment %d, run %d, OK" % (experiment, run))
            else:
                print("\n--Experiment %d, run %d, FAILED" % (experiment, run))
            dumpstates()
    print("DONE.")
    
    
if __name__ == "__main__":
    main()    