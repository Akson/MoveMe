#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.ObjectWithText import ObjectWithText
from MoveMe.Canvas.Objects.Base.ClonableObject import ClonableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject

import wx
import numpy as np

class BaseNode(ObjectWithText, ClonableObject, DeletableObject, SelectableObject, MovableObject):
    def __init__(self, **kwargs):
        super(BaseNode, self).__init__(**kwargs)

        self.boundingBoxDimensions = kwargs.get("boundingBoxDimensions", [90, 30])
        self.nodeBackgroundColor = '#EEEEEE'
        self.parametersForSaving.append("text")

    def Render(self, gc):
        gc.SetBrush(wx.Brush(self.nodeBackgroundColor, wx.SOLID))
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1], 10)
        
        if self.connectableSource:
            for connection in self.GetOutcomingConnections():
                connection.Render(gc)
        
        self.DrawText(gc)

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
        if self.connectableSource:
            for connection in self._outcomingConnections:
                connection.destination.DeleteIncomingConnection(connection)
        if self.connectableDestination:
            for connection in self._incomingConnections:
                connection.source.DeleteOutcomingConnection(connection)
    
    def DrawText(self, gc):
        gc.Clip(self.position[0], self.position[1], self.boundingBoxDimensions[0], self.boundingBoxDimensions[1])
        gc.SetFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))
        gc.DrawText(self.text, self.position[0]+5, self.position[1]+5)