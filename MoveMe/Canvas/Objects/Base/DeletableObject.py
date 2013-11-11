#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class DeletableObject(CanvasObject):
    def __init__(self, **kwargs):
        super(DeletableObject, self).__init__(**kwargs)
        self.deletable = True
        
    def Delete(self):
        """
        Delete method is called when an object is deleted from a canvas.
        """
        raise NotImplementedError()