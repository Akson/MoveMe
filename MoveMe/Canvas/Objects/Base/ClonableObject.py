#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class ClonableObject(CanvasObject):
    def __init__(self, **kwargs):
        super(ClonableObject, self).__init__(**kwargs)
        self.clonable = True

    def GetCloningNodeDescription(self):
        """
        GetNodeDescription should return a dictionary that contains 
        all information required for cloning this node at another position
        """
        raise NotImplementedError()
