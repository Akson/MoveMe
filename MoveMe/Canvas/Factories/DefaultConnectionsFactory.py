#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Connection import Connection
from MoveMe.Canvas.Factories.ConnectionsFactoryInterface import ConnectionsFactoryInterface

class DefaultConnectionsFactory(ConnectionsFactoryInterface):
    def __init__(self):
        pass
    
    def CreateConnectionBetweenNodesFromDescription(self, source, destination, connectionDescription=None):
        return Connection(source, destination)