import SPP_aux
import SPP_exceptions

class EncounterAlgorithm:
    """Abstract class of encounter algorithms"""
    def execute(self,nodes,maxnodeval):
        raise SPP_exceptions.AbstractException
    
class Max(EncounterAlgorithm):
    """Algorithm to find maximum value between agents"""
    
    def execute(self, node1, node2):
        """Specifies the algorithm to use when two nodes collide."""
        node1.value = SPP_aux.getmax(node1.value, node2.value)
    
    def __str__(self):
        return "max"
    
algorithms=[Max()]