#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject

class SimpleBoxNode(DeletableObject, SelectableObject, MovableObject, CanvasObject):
    """
    SimpleBoxNode class represents a simplest possible canvas object 
    that is basically a rectangular box.
    """
    def __init__(self, **kwargs):
        super(SimpleBoxNode, self).__init__(**kwargs)
        self.boundingBoxDimensions = [90, 60]

    def Render(self, gc):
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1], 10)
        gc.SetFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))
        gc.DrawText("(%d, %d)"%(self.position[0], self.position[1]), self.position[0]+10, self.position[1]+10)

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