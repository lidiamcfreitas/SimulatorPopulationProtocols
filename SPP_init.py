import SPP_aux

class InitAlgorithm:
    """Abstract class of initializors"""
    def execute(self,nodes,maxnodeval):
        raise SPP_exceptions.AbstractException
    
class AllNodesEqual(InitAlgorithm):
    """Initializes all agents with the same value"""
    def __init__(self):
        super(AllNodesEqual, self)
    
    def execute(self,nodes,maxnodeval):
        maxInNetwork = SPP_aux.selectRandomInt(maxnodeval)
        for node in nodes:
            node.setValue(maxInNetwork)
        return maxInNetwork
    
    def __str__(self):
        return "all nodes equal"

class AllNodesDif(InitAlgorithm):
    """Initializes all agents with different values from 0 to maxnodeval"""
    def __init__(self):
        super(AllNodesDif, self)
    
    def execute(self,nodes,maxnodeval):
        maxInNetwork = -1
        for node in nodes:
            randomVal = SPP_aux.selectRandomInt(maxnodeval)
            maxInNetwork = SPP_aux.getmax(maxInNetwork, randomVal)
            node.value = randomVal
        return maxInNetwork
    
    def __str__(self):
        return "all nodes different"