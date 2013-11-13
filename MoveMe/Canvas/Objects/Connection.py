#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
import wx
import numpy as np

class Connection(CanvasObject):
    def __init__(self, source, destination, **kwargs):
        super(Connection, self).__init__(**kwargs)

        self.source = source
        self.destination = destination
        self.arrowWidth = kwargs.get("arrowWidth", 5)
        self.arrowLength = kwargs.get("arrowLength", 10)

    def Render(self, gc):
        gc.SetPen(wx.Pen('#000000', 1, wx.SOLID))
        self.RenderArrow(gc, self.SourcePoint(), self.DestinationPoint())

    def RenderHighlighting(self, gc):
        return

    def ReturnObjectUnderCursor(self, pos):
        return None
    
    def RenderArrow(self, gc, sourcePoint, destinationPoint):
        gc.DrawLines([sourcePoint, destinationPoint])
        
        #Draw arrow
        p0 = np.array(sourcePoint)
        p1 = np.array(destinationPoint)
        dp = p0-p1
        l = np.linalg.norm(dp)
        dp = dp / l
        n = np.array([-dp[1], dp[0]])
        neck = p1 + self.arrowLength*dp
        lp = neck + n*self.arrowWidth
        rp = neck - n*self.arrowWidth
        
        gc.DrawLines([lp, destinationPoint])
        gc.DrawLines([rp, destinationPoint])

    def SourcePoint(self):
        return np.array(self.source.GetConnectionPortForTargetPoint(self.destination.GetCenter()))
    
    def DestinationPoint(self):
        return np.array(self.destination.GetConnectionPortForTargetPoint(self.source.GetCenter()))

