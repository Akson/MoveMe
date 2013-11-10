#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class MovableObject(CanvasObject):
    def __init__(self, position):
        super(MovableObject, self).__init__()
        self.position = position
        
        self.movable = True