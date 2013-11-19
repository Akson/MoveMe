#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.BaseNode import BaseNode
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination

class DestinationNode(BaseNode, ConnectableDestination):
    def __init__(self, **kwargs):
        super(DestinationNode, self).__init__(**kwargs)
        self.nodeBackgroundColor = '#FFDDDD'

    def ReturnObjectUnderCursor(self, pos):
        if self.IsPointInside(pos): 
            return self

        return None

    def ReceiveMessage(self, message):
        """"This is a destination node, so it should process all incoming messages here"""
        raise NotImplementedError()