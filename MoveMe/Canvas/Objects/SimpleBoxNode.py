#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.ClonableObject import ClonableObject
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination
from MoveMe.Canvas.Objects.Base.ConnectableSource import ConnectableSource

class SimpleBoxNode(ConnectableSource, ConnectableDestination, ClonableObject, DeletableObject, SelectableObject, MovableObject, CanvasObject):
    """
    SimpleBoxNode class represents a simplest possible canvas object 
    that is basically a rectangular box.
    """
    def __init__(self, **kwargs):
        super(SimpleBoxNode, self).__init__(**kwargs)
        self.boundingBoxDimensions = kwargs.get("boundingBoxDimensions", [90, 30])

    def Render(self, gc):
        gc.SetBrush(wx.Brush('#EEEEEE', wx.SOLID))
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1], 10)
        
        for connection in self.GetOutcomingConnections():
            connection.Render(gc)

    def RenderHighlighting(self, gc):
        gc.SetBrush(wx.Brush('#888888', wx.TRANSPARENT))
        gc.SetPen(wx.Pen('#888888', 3, wx.DOT))
        gc.DrawRectangle(self.position[0]-3, 
                         self.position[1]-3, 
                         self.boundingBoxDimensions[0]+6, 
                         self.boundingBoxDimensions[1]+6)

    def RenderSelection(self, gc):
        gc.SetBrush(wx.Brush('#888888', wx.TRANSPARENT))
        gc.SetPen(wx.Pen('#CC0000', 3, wx.DOT))
        gc.DrawRectangle(self.position[0]-2, 
                         self.position[1]-2, 
                         self.boundingBoxDimensions[0]+4, 
                         self.boundingBoxDimensions[1]+4)
        
    def ReturnObjectUnderCursor(self, pos):
        #Check if a position is inside of a rectangle
        if pos[0] < self.position[0]: return None
        if pos[1] < self.position[1]: return None
        if pos[0] > self.position[0]+self.boundingBoxDimensions[0]: return None
        if pos[1] > self.position[1]+self.boundingBoxDimensions[1]: return None
        return self
    
    def Delete(self):
        pass