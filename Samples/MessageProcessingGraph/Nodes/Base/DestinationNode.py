#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination
from MessageProcessingGraph.Nodes.Base.BaseNode import BaseNode

class DestinationNode(BaseNode, ConnectableDestination):
    def __init__(self):
        super(DestinationNode, self).__init__()
        self.nodeBackgroundColor = '#FFDDDD'

    def ReturnObjectUnderCursor(self, pos):
        if self.IsPointInside(pos): 
            return self

        return None

    def ReceiveMessage(self, message):
        """"This is a destination node, so it should process all incoming messages here"""
        raise NotImplementedError()
    
    def GetListOfAllPossibleConnectionsSources(self):
        return None