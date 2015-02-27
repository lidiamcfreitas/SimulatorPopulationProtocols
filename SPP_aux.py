import random
random.seed() # initializes the seed with the current system time (default)

def getmax(i,j):
    """ Returns the maximum value of i and j."""
    return (i,j)[i<j] # true - 1; false - 0

def selectRandomInt(maxvalue):
    """ Selects a random value between 0 and (maxvalue-1)."""
    return int(random.random()*maxvalue)

def selectRandomNode(nodes):
    """ Selects a random node by returning it's index."""
    return nodes[selectRandomInt(len(nodes))]