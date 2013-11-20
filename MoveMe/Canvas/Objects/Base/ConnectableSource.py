#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.ConnectableObject import ConnectableObject

class ConnectableSource(ConnectableObject):
    def __init__(self):
        super(ConnectableSource, self).__init__()
        self.connectableSource = True
        
        self._outcomingConnections = []
        
    def AddOutcomingConnection(self, connection):
        self._outcomingConnections.append(connection)
    
    def DeleteOutcomingConnection(self, connection):
        self._outcomingConnections.remove(connection)
        
    def GetOutcomingConnections(self):
        return self._outcomingConnections