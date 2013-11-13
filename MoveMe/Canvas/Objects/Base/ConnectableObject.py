#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject

class ConnectableObject(CanvasObject):
    def __init__(self, **kwargs):
        super(ConnectableObject, self).__init__(**kwargs)

    def GetConnectionPortForTargetPoint(self, targetPoint):
        """
        GetConnectionPortForTargetPoint method should return an end 
        point position for a connection object.
        """
        raise NotImplementedError()
    
    def GetCenter(self):
        """
        GetCenter method should return a center of this object. 
        It is used during a connection process as a preview of a future connection.
        """
        raise NotImplementedError()
    
