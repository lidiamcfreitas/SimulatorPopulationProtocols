import SPP_aux
import SPP_exceptions



class AssertAlgorithm:
    """Abstract class of assert algorithms"""
    def execute(self,nodes,maxnodeval):
        raise SPP_exceptions.AbstractException
    
class AllEqual(AssertAlgorithm):
    """Algorithm to assert if values of agents are equal"""
    
    def execute(self, maxInNetwork,nodes):
        """Verifies the value of the nodes to equal maxInNetwork. 0-incorrect.1-correct."""
        if (maxInNetwork>0):
            for node in nodes:
                if (node.value != maxInNetwork):
                    return 0
            return 1
        return 0
    
    def __str__(self):
        return "equal"
    
algorithms=[AllEqual()]