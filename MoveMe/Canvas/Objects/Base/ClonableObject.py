#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class ClonableObject(CanvasObject):
    def __init__(self):
        super(ClonableObject, self).__init__()
        self.clonable = True
        self.parametersForSaving = []

    def GetCloningNodeDescription(self):
        """
        GetNodeDescription should return a dictionary that contains 
        all information required for cloning this node at another position
        """
        nodeDescription = {}
        nodeDescription["NodeClass"] = self.__class__.__name__
        
        nodeParameters = {}
        for parameter in self.parametersForSaving:
            nodeParameters[parameter] = self.__dict__[parameter]
        nodeDescription["NodeParameters"] = nodeParameters 
        
        return nodeDescription