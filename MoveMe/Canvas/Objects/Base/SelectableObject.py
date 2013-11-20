#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class SelectableObject(CanvasObject):
    def __init__(self):
        super(SelectableObject, self).__init__()
        self.selectable = True

    def RenderSelection(self, gc):
        """
        RenderHighlighting method should draw an 
        object with a selection border around it.
        """
        raise NotImplementedError()