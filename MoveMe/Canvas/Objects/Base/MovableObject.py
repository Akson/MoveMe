#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class MovableObject(CanvasObject):
    def __init__(self, **kwargs):
        super(MovableObject, self).__init__(**kwargs)
        self.movable = True
        
        self.position = kwargs.get("position", [0,0])