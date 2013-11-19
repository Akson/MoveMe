#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.BaseNode import BaseNode
from MoveMe.Canvas.Objects.Base.ConnectableSource import ConnectableSource
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination

class IntermediateNode(BaseNode, ConnectableSource, ConnectableDestination):
    def __init__(self, **kwargs):
        super(IntermediateNode, self).__init__(**kwargs)
        self.nodeBackgroundColor = '#EEEEEE'

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
    
    def ReceiveMessage(self, message):
        processedMessage = self.ProcessMessage(message)
        if processedMessage:
            self.SendMessage(message)
            
    def ProcessMessage(self, message):
        """
        Processes a message and returns it. 
        Returns None if there is no need to continue processing this message.
        """
        raise NotImplementedError()