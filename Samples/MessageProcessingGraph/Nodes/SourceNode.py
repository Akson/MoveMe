#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.BaseNode import BaseNode
from MoveMe.Canvas.Objects.Base.ConnectableSource import ConnectableSource

class SourceNode(BaseNode, ConnectableSource):
    def __init__(self, **kwargs):
        super(SourceNode, self).__init__(**kwargs)
        self.nodeBackgroundColor = '#DDFFDD'

    def ReturnObjectUnderCursor(self, pos):
        if self.IsPointInside(pos): 
            return self
        
        for connection in self._outcomingConnections:
            connectionComponent = connection.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        return None

    def SendMessage(self, message):
        for connection in self.GetOutcomingConnections():
            connection.destination.ReceiveMessage(message)
