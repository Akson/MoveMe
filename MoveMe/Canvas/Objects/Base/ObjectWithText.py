#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class ObjectWithText(CanvasObject):
    def __init__(self, **kwargs):
        super(ObjectWithText, self).__init__(**kwargs)
        
        self.text = kwargs.get("text", self.__class__.__name__)