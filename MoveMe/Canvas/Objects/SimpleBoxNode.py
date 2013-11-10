#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx

class SimpleBoxNode(object):
    """
    SimpleBoxNode class represents a simplest possible canvas object 
    that is basically a rectangular box.
    """
    def __init__(self, pos):
        self.position = pos
        self.boundingBoxDimensions = [90, 60]

    def Render(self, gc):
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1], 10)
        gc.SetFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))
        gc.DrawText("(%d, %d)"%(self.position[0], self.position[1]), self.position[0]+10, self.position[1]+10)