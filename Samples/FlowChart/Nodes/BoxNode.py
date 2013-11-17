#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from FlowChart.Nodes.ConnectionPort import ConnectionPort
from MoveMe.Canvas.Objects.SimpleBoxNode import SimpleBoxNode

class BoxNode(SimpleBoxNode):
    def __init__(self, **kwargs):
        super(BoxNode, self).__init__(**kwargs)
        self.connectableSource = False
        self.connectableDestination = False

        self.connectionPorts = [ConnectionPort(self), ConnectionPort(self), ConnectionPort(self), ConnectionPort(self)]

    def UpdateConnectionPortsPositions(self):
        #top
        self.connectionPorts[0].relativeCenterPosition = [0.5*self.boundingBoxDimensions[0], 0]
        #bottom
        self.connectionPorts[1].relativeCenterPosition = [0.5*self.boundingBoxDimensions[0], self.boundingBoxDimensions[1]]
        #left
        self.connectionPorts[2].relativeCenterPosition = [0, 0.5*self.boundingBoxDimensions[1]]
        #right
        self.connectionPorts[3].relativeCenterPosition = [self.boundingBoxDimensions[0], 0.5*self.boundingBoxDimensions[1]]

    def Render(self, gc):
        super(BoxNode, self).Render(gc)
        
        self.UpdateConnectionPortsPositions()
        for connectionPort in self.connectionPorts:
            connectionPort.Render(gc)

    def RenderHighlighting(self, gc):
        super(BoxNode, self).RenderHighlighting(gc)

        self.UpdateConnectionPortsPositions()
        for connectionPort in self.connectionPorts:
            connectionPort.RenderBox(gc)

    def ReturnObjectUnderCursor(self, pos):
        for connectionPort in self.connectionPorts:
            connectionComponent = connectionPort.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        if self.IsPointInside(pos): 
            return self
        
        return None

    def GetCloningNodeDescription(self):
        return "text"
    
    def Delete(self):
        for connectionPort in self.connectionPorts:
            connectionPort.Delete()