import random


maxnodes = 4
experiments =2
runsPerExp = 10
roundsPerRun = 10
maxnodeval = 200

nodes = []

def dumpstates():
    string = ""
    for i in range(len(nodes)):
        print("----Node[%d].my_val=%d;" % (i,nodes[i].value))

def selectRandomInt(maxvalue):
    return int(random.random()*maxvalue)

def selectRandomNode():
    return selectRandomInt(maxnodes)

def initnodes(algorithm):
    return algorithm.execute()

def getmax(i,j):
    return (i,j)[i<j] # true - 1; false - 0

def assertAlgo(maxInNetwork):
    
    if (maxInNetwork>0):
        for node in nodes:
            if (node.value != maxInNetwork):
                return 0
        return 1
    return 0

def encounter( i, j):
    nodes[i].value = getmax(nodes[i].value, nodes[j].value)


class ErrorAlgorithm(Exception):
    def __str__(self):
        return "Please implement all the methods"

class Node:
    
    def __init__(self):
        self.value = selectRandomInt(maxnodeval)
    
    def setValue(self, val):
        self.value = val

class Algorithm:
    
    def execute(self):
        raise ErrorAlgorithm
    
class AllNodesEqual(Algorithm):

    def __init__(self):
        super(AllNodesEqual, self)
    
    def execute(self):
        maxInNetwork = selectRandomInt(maxnodeval)
        for node in nodes:
            node.setValue(maxInNetwork)
        return maxInNetwork
    
    def __str__(self):
        return "all nodes equal"

class AllNodesDif(Algorithm):

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
                print("--Experiment %d, run %d, OK" % (experiment, run))
            else:
                print("--Experiment %d, run %d, FAILED" % (experiment, run))
            dumpstates()
    print("DONE.")
    
    
if __name__ == "__main__":
    main()    