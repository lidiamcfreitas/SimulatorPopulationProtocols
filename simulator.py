import SPP_io
import SPP_exceptions
import SPP_init
import SPP_aux
import SPP_encounter
import SPP_assert

# 4,2,10,10,200

def initnodes(algorithm):
    """ Initializes the nodes given an algorithm."""
    return algorithm.execute(nodes,maxnodeval)


class Node:
    """Class node defines an agent."""
    def __init__(self):
        self.value = SPP_aux.selectRandomInt(maxnodeval)
    
    def setValue(self, val):
        self.value = val
        
class Experiment:
    def __init__(self,var_init,var_encounter,var_assert):
        for algo in SPP_init.algorithms:
            if (algo.__str__() == var_init):
                self._init = algo
        for algo in SPP_encounter.algorithms:
            if (algo.__str__() == var_encounter):
                self._encounter = algo        
        for algo in SPP_assert.algorithms:
            if (algo.__str__() == var_assert):
                self._assert = algo
    def __str__(self):
        return "[init: %s, encounter: %s, assert: %s]" % (var_init, var_encounter, var_assert)
# MAIN #


def experiment():
    
    global nodes 
    global maxnodes
    global var_init
    global var_encounter
    global var_assert
    global runsPerExp
    global roundsPerRun
    global maxnodeval
    
    maxnodes= eval(maxnodes)
    runsPerExp = eval(runsPerExp)
    roundsPerRun = eval(roundsPerRun)
    maxnodeval = eval(maxnodeval)
    
    
    nodes = []
    for i in range(maxnodes):
        nodes += [Node()]
    
    experiment = Experiment(var_init, var_encounter, var_assert)   
    print("STARTING %s experiment, for %d runs\n" % (Experiment, runsPerExp))
    
    for run in range(runsPerExp):
        maxInNetwork = initnodes(experiment._init)
        
        for round in range(roundsPerRun):
            node1 = SPP_aux.selectRandomNode(nodes)
            node2 = SPP_aux.selectRandomNode(nodes)
            experiment._encounter.execute(node1,node2)
            
        if (experiment._assert.execute(maxInNetwork,nodes)):
            print("\n--Experiment %s, run %d, OK" % (experiment, run))
        else:
            print("\n--Experiment %s, run %d, FAILED" % (experiment, run))
        SPP_io.dumpstates(nodes)
    
    print("DONE.")
    
def main():
    global nodes 
    global maxnodes
    global var_init
    global var_encounter
    global var_assert
    global runsPerExp
    global roundsPerRun
    global maxnodeval
    
    test = SPP_io.readvalues("specifications.txt")
    for t in test:
        print("______________________TEST______________________")
        maxnodes, var_init, var_encounter, var_assert, runsPerExp, roundsPerRun, maxnodeval = t
        print("NODES:",maxnodes)
        experiment()
    
    
if __name__ == "__main__":
    main()    