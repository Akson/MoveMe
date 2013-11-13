#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.ConnectableObject import ConnectableObject

class ConnectableDestination(ConnectableObject):
    def __init__(self, **kwargs):
        super(ConnectableDestination, self).__init__(**kwargs)
        self.connectableDestination = True
        
        self._incomingConnections = []
        
    def AddIncomingConnection(self, connection):
        self._incomingConnections.append(connection)
        
    def DeleteIncomingConnection(self, connection):
        self._incomingConnections.remove(connection)
