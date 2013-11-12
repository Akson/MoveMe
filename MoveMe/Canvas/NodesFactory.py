#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.SimpleTextBoxNode import SimpleTextBoxNode

class NodesFactory(object):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        return SimpleTextBoxNode(text=nodeDescription)