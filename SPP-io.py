
def dumpstates():
    """ Prints the nodes representation."""
    string = ""
    for i in range(len(nodes)):
        print("----Node[%d].my_val=%d;" % (i,nodes[i].value))
        

def readvalues(filename):
    file = open(filename,"r")
    for line in file:
        results = line[:-1].split(",")
        results = tuple([int(elem) for elem in results])
    return results
    