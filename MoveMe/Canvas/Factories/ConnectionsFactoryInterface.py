#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)

class ConnectionsFactoryInterface(object):
    def __init__(self):
        pass
    
    def CreateConnectionBetweenNodesFromDescription(self, source, destination, connectionDescription=None):
        """
        CreateConnectionBetweenNodesFromDescription returns a newly created connection
        based on provided source, destinations and description. 
        connectionDescription may be None.
        May return None if it is not possible to make a connection
        """
        raise NotImplementedError()