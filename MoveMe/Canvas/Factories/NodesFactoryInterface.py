#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)

class NodesFactoryInterface(object):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        """
        CreateNodeFromDescription returns a newly created node based on a provided node description.
        May return None if it is not possible to create a node.
        """
        raise NotImplementedError()
