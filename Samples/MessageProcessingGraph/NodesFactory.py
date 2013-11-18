#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
from MessageProcessingGraph.Nodes.BaseNode import BaseNode

class NodesFactory(NodesFactoryInterface):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        return BaseNode(text=nodeDescription)