def dumpstates(nodes):
    """ Prints the nodes representation."""
    string = ""
    for i in range(len(nodes)):
        print("----Node[%d].my_val=%d;" % (i,nodes[i].value))
        

def readvalues(filename):
    """reads input configuration from filename"""
    file = open(filename,"r")
    res = []
    for line in file:
        results = line[:-1].split(",")
        res += [tuple([int(elem) for elem in results])]
    return res