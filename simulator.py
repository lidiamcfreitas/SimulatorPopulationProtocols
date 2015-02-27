import SPP_io
import SPP_exceptions
import SPP_init
import SPP_aux
import SPP_encounter
import SPP_assert

def initnodes(algorithm):
    """ Initializes the nodes given an algorithm."""
    return algorithm.execute(nodes,maxnodeval)


class Node:
    """Class node defines an agent."""
    def __init__(self):
        self.value = SPP_aux.selectRandomInt(maxnodeval)
    
    def setValue(self, val):
        self.value = val
    

# MAIN #


def experiment():
    
    global nodes 
    global maxnodes
    global experiments
    global runsPerExp
    global roundsPerRun
    global maxnodeval
    
    nodes = []
    for i in range(maxnodes):
        nodes += [Node()]
        
    print("STARTING %d experiments, %d runs each\n" % (experiments, runsPerExp))
    
    exps = [SPP_init.AllNodesEqual(), SPP_init.AllNodesDif()]
    
    for experiment in range(experiments):
        for run in range(runsPerExp):
            maxInNetwork = initnodes(exps[experiment])
            
            for round in range(roundsPerRun):
                node1 = SPP_aux.selectRandomNode(nodes)
                node2 = SPP_aux.selectRandomNode(nodes)
                SPP_encounter.Max().encounter(node1,node2)
                
            if (SPP_assert.AllEqual().execute(maxInNetwork,nodes)):
                print("\n--Experiment %d, run %d, OK" % (experiment, run))
            else:
                print("\n--Experiment %d, run %d, FAILED" % (experiment, run))
            SPP_io.dumpstates(nodes)
    print("DONE.")
    
def main():
    global nodes 
    global maxnodes
    global experiments
    global runsPerExp
    global roundsPerRun
    global maxnodeval
    
    test = SPP_io.readvalues("specifications.txt")
    for t in test:
        print("______________________TEST______________________")
        maxnodes, experiments, runsPerExp, roundsPerRun, maxnodeval = t
        print("NODES:",maxnodes)
        experiment()
    
    
if __name__ == "__main__":
    main()    