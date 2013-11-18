#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.ClonableObject import ClonableObject
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination
from MoveMe.Canvas.Objects.Base.ConnectableSource import ConnectableSource

import numpy as np

class SimpleBoxNode(ConnectableSource, ConnectableDestination, ClonableObject, DeletableObject, SelectableObject, MovableObject, CanvasObject):
    """
    SimpleBoxNode class represents a simplest possible canvas object 
    that is basically a rectangular box.
    """
    def __init__(self, **kwargs):
        super(SimpleBoxNode, self).__init__(**kwargs)
        self.boundingBoxDimensions = kwargs.get("boundingBoxDimensions", [90, 30])

    def Render(self, gc):
        super(SimpleBoxNode, self).Render(gc)
        gc.SetBrush(wx.Brush('#EEEEEE', wx.SOLID))
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1], 10)

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
        if self.IsPointInside(pos): 
            return self
        
        for connection in self._outcomingConnections:
            connectionComponent = connection.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        return None

    def IsPointInside(self, pos):
        if pos[0] < self.position[0]: return False
        if pos[1] < self.position[1]: return False
        if pos[0] > self.position[0]+self.boundingBoxDimensions[0]: return False
        if pos[1] > self.position[1]+self.boundingBoxDimensions[1]: return False
        return True
    
    def GetConnectionPortForTargetPoint(self, targetPoint):
        targetPoint = np.array(targetPoint)
        center = np.array(self.GetCenter())
        direction = targetPoint - center
        
        if direction[0] > 0:
            #Check right border
            borderX = self.position[0] + self.boundingBoxDimensions[0] 
        else:
            #Check left border
            borderX = self.position[0]
        if direction[0] == 0:
            t1 = float("inf")
        else:
            t1 = (borderX - center[0]) / direction[0] 
        
        
        if direction[1] > 0:
            #Check bottom border
            borderY = self.position[1] + self.boundingBoxDimensions[1] 
        else:
            #Check top border
            borderY = self.position[1]
        if direction[1] == 0: 
            t2 = float("inf")
        else:
            t2 = (borderY - center[1]) / direction[1]
        
        t = min(t1, t2)
        boundaryPoint = center + t*direction

        return boundaryPoint
    
    def GetCenter(self):
        return [self.position[0] + 0.5*self.boundingBoxDimensions[0], self.position[1] + 0.5*self.boundingBoxDimensions[1]]
    
    def Delete(self):
        for connection in self._outcomingConnections:
            connection.destination.DeleteIncomingConnection(connection)
        for connection in self._incomingConnections:
            connection.source.DeleteOutcomingConnection(connection)