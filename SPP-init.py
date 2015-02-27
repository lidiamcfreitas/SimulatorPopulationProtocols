class InitAlgorithm:
    """Abstract class of initializors"""
    def execute(self):
        raise SPP_exceptions.AbstractException
    
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