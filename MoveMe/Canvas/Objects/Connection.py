#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
import wx
import numpy as np
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject

class Connection(SelectableObject, DeletableObject, CanvasObject):
    def __init__(self, source, destination, **kwargs):
        super(Connection, self).__init__(**kwargs)

        self.source = source
        self.destination = destination
        self.arrowWidth = kwargs.get("arrowWidth", 3)
        self.arrowLength = kwargs.get("arrowLength", 12)

    def Render(self, gc):
        gc.SetPen(wx.Pen('#000000', 1, wx.SOLID))
        self.RenderArrow(gc, self.SourcePoint(), self.DestinationPoint())

    def RenderHighlighting(self, gc):
        gc.SetPen(wx.Pen('#888888', 4, wx.DOT))
        self.RenderArrow(gc, self.SourcePoint(), self.DestinationPoint())
        
    def RenderSelection(self, gc):
        gc.SetBrush(wx.Brush('#888888', wx.TRANSPARENT))
        gc.SetPen(wx.Pen('#CC0000', 3, wx.SOLID))
        self.RenderArrow(gc, self.SourcePoint(), self.DestinationPoint())
    
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

    def Delete(self):
        self.source.DeleteOutcomingConnection(self)
        self.destination.DeleteIncomingConnection(self)

    def ReturnObjectUnderCursor(self, pos):
        return self if self.IsPointInside(pos) else None

    def IsPointInside(self, pos):
        d = self.DistToLineSegment(self.SourcePoint(), self.DestinationPoint(), np.array(pos))
        return True if d<3 else False
    
    def DistToLineSegment(self, src, dst, pos):
        lengthSq = (dst-src)[0]*(dst-src)[0]+(dst-src)[1]*(dst-src)[1]
        if lengthSq == 0: return np.linalg.norm(dst-pos)
            
        t = np.dot(pos-src, dst-src)/lengthSq
        if t<0: return np.linalg.norm(src-pos)
        if t>1: return np.linalg.norm(dst-pos)
        
        proj = src + t * (dst-src)
        return np.linalg.norm(proj-pos)

