#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
import logging

class DefaultNodesFactory(NodesFactoryInterface):
    def __init__(self, supportedClasses = {}):
        if type(supportedClasses)!=dict:
            raise TypeError("supportedClasses should be a dictionary")
        self.supportedClasses = supportedClasses
    
    def CreateNodeFromDescription(self, nodeDescription):
        if type(nodeDescription) != dict:
            logging.debug("Node description should be a dictionary")
            return None
        
        if "NodeClass" not in nodeDescription:
            logging.debug("This nodes factory require NodeClass field for constructing a node")
            return None

        if nodeDescription["NodeClass"] not in self.supportedClasses:
            logging.debug("This class is not supported")
            return None 

        try:
            nodeClass = self.supportedClasses[nodeDescription["NodeClass"]]
            node = nodeClass()
            
            if "NodeParameters" in nodeDescription:
                if type(nodeDescription["NodeParameters"]) == dict:
                    node.__dict__.update(nodeDescription["NodeParameters"])
                else:
                    logging.warning("NodeParameters should be a dictionary")
            
            return node
        
        except:
            return None