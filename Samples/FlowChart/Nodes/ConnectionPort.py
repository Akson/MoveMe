#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.Base.ConnectableDestination import ConnectableDestination
from MoveMe.Canvas.Objects.Base.ConnectableSource import ConnectableSource
from wx import wx

class ConnectionPort(ConnectableSource, ConnectableDestination):
    def __init__(self, parent, **kwargs):
        super(ConnectionPort, self).__init__(**kwargs)
        self.parent = parent
        self.relativeCenterPosition = kwargs.get("relativeCenterPosition", [0, 0])
        self.size = kwargs.get("size", 6)
    
    def Render(self, gc):
        for connection in self.GetOutcomingConnections():
            connection.Render(gc)

    def RenderBox(self, gc):
        gc.SetBrush(wx.Brush('#5555FF', wx.SOLID))
        gc.SetPen(wx.TRANSPARENT_PEN)
        gc.DrawRectangle(self.parent.position[0]+self.relativeCenterPosition[0]-self.size/2, 
                         self.parent.position[1]+self.relativeCenterPosition[1]-self.size/2, 
                         self.size, 
                         self.size,)

    def RenderHighlighting(self, gc):
        gc.SetBrush(wx.Brush('#5555FF', wx.SOLID))
        gc.SetPen(wx.TRANSPARENT_PEN)
        gc.DrawRectangle(self.parent.position[0]+self.relativeCenterPosition[0]-self.size/2, 
                         self.parent.position[1]+self.relativeCenterPosition[1]-self.size/2, 
                         self.size, 
                         self.size,)
        gc.SetBrush(wx.TRANSPARENT_BRUSH)
        gc.SetPen(wx.Pen('#888888', 3, wx.DOT))
        gc.DrawRectangle(self.parent.position[0]+self.relativeCenterPosition[0]-self.size/2-3, 
                         self.parent.position[1]+self.relativeCenterPosition[1]-self.size/2-3, 
                         self.size+6, 
                         self.size+6,)

    def ReturnObjectUnderCursor(self, pos):
        if self.IsPointInside(pos): 
            return self
        
        for connection in self._outcomingConnections:
            connectionComponent = connection.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        return None

    def IsPointInside(self, pos):
        if pos[0] < self.parent.position[0]+self.relativeCenterPosition[0]-self.size/2: return False
        if pos[1] < self.parent.position[1]+self.relativeCenterPosition[1]-self.size/2: return False
        if pos[0] > self.parent.position[0]+self.relativeCenterPosition[0]+self.size/2: return False
        if pos[1] > self.parent.position[1]+self.relativeCenterPosition[1]+self.size/2: return False
        return True

    def GetConnectionPortForTargetPoint(self, targetPoint):
        return self.GetCenter()
    
    def GetCenter(self):
        return [self.parent.position[0]+self.relativeCenterPosition[0], self.parent.position[1]+self.relativeCenterPosition[1]]
    
    def Delete(self):
        for connection in self._outcomingConnections:
            connection.destination.DeleteIncomingConnection(connection)
        for connection in self._incomingConnections:
            connection.source.DeleteOutcomingConnection(connection)