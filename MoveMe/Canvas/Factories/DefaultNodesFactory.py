#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
import logging

class DefaultNodesFactory(NodesFactoryInterface):
    def __init__(self, supportedClassesList = []):
        if type(supportedClassesList)!=list:
            raise TypeError("supportedClassesList should be a list")
        
        self.supportedClasses = {}
        for curClass in supportedClassesList:
            self.supportedClasses[curClass.__name__] = curClass
    
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

        nodeClass = self.supportedClasses[nodeDescription["NodeClass"]]
        node = nodeClass()
            
        if "NodeParameters" in nodeDescription:
            if type(nodeDescription["NodeParameters"]) == dict:
                node.LoadObjectFromDict(nodeDescription["NodeParameters"])
            else:
                logging.warning("NodeParameters should be a dictionary")
        
        return node
        
