#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class ObjectWithText(CanvasObject):
    def __init__(self, text=None):
        super(ObjectWithText, self).__init__()
        self.text = self.__class__.__name__ if text==None else text