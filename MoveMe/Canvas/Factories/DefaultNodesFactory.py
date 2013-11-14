#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.SimpleTextBoxNode import SimpleTextBoxNode
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface

class DefaultNodesFactory(NodesFactoryInterface):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        return SimpleTextBoxNode(text=nodeDescription)