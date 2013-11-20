#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from FlowChart.Nodes.ConnectionPort import ConnectionPort
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
from MoveMe.Canvas.Objects.Base.ClonableObject import ClonableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject

class NodeWith4ConnectionPorts(ClonableObject, DeletableObject, SelectableObject, MovableObject, CanvasObject):
    def __init__(self, **kwargs):
        super(NodeWith4ConnectionPorts, self).__init__(**kwargs)

        self.connectionPorts = [ConnectionPort(self), ConnectionPort(self), ConnectionPort(self), ConnectionPort(self)]

    def Render(self, gc):
        self.RenderMainShape(gc)
        
        self.UpdateConnectionPortsPositions()
        for connectionPort in self.connectionPorts:
            connectionPort.Render(gc)

    def RenderHighlighting(self, gc):
        self.RenderMainShapeHighlighting(gc)

        self.UpdateConnectionPortsPositions()
        for connectionPort in self.connectionPorts:
            connectionPort.RenderBox(gc)

    def RenderSelection(self, gc):
        self.RenderMainShapeSelection(gc)

    def ReturnObjectUnderCursor(self, pos):
        for connectionPort in self.connectionPorts:
            connectionComponent = connectionPort.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        if self.IsPointInside(pos): 
            return self
        
        return None

    def Delete(self):
        for connectionPort in self.connectionPorts:
            connectionPort.Delete()


    def IsPointInside(self, pos):
        raise NotImplementedError()
    
    def UpdateConnectionPortsPositions(self):
        raise NotImplementedError()

    def RenderMainShape(self, gc):
        raise NotImplementedError()

    def RenderMainShapeHighlighting(self, gc):
        raise NotImplementedError()

    def RenderMainShapeSelection(self, gc):
        raise NotImplementedError()
