#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
import wx

class Connection(CanvasObject):
    def __init__(self, source, destination, **kwargs):
        super(Connection, self).__init__(**kwargs)

        self.source = source
        self.destination = destination

    def Render(self, gc):
        gc.SetPen(wx.Pen('#000000', 1, wx.SOLID))
        gc.DrawLines([self.source.position, self.destination.position])

    def RenderHighlighting(self, gc):
        return

    def ReturnObjectUnderCursor(self, pos):
        return None