#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from FlowChart.Nodes.NodeWithConnectionPorts import NodeWith4ConnectionPorts
from MoveMe.Canvas.Objects.Base.ObjectWithText import ObjectWithText

class BoxNode(ObjectWithText, NodeWith4ConnectionPorts):
    def __init__(self, **kwargs):
        super(BoxNode, self).__init__(**kwargs)
        self.boundingBoxDimensions = kwargs.get("boundingBoxDimensions", [90, 30])
        self.parametersForSaving.append("text")
        self.parametersForSaving.append("boundingBoxDimensions")

    def IsPointInside(self, pos):
        if pos[0] < self.position[0]: return False
        if pos[1] < self.position[1]: return False
        if pos[0] > self.position[0]+self.boundingBoxDimensions[0]: return False
        if pos[1] > self.position[1]+self.boundingBoxDimensions[1]: return False
        return True
    
    def UpdateConnectionPortsPositions(self):
        #top
        self.connectionPorts[0].relativeCenterPosition = [0.5*self.boundingBoxDimensions[0], 0]
        #bottom
        self.connectionPorts[1].relativeCenterPosition = [0.5*self.boundingBoxDimensions[0], self.boundingBoxDimensions[1]]
        #left
        self.connectionPorts[2].relativeCenterPosition = [0, 0.5*self.boundingBoxDimensions[1]]
        #right
        self.connectionPorts[3].relativeCenterPosition = [self.boundingBoxDimensions[0], 0.5*self.boundingBoxDimensions[1]]

    def RenderMainShape(self, gc):
        gc.SetBrush(wx.Brush('#EEEEEE', wx.SOLID))
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRectangle(self.position[0], 
                                self.position[1], 
                                self.boundingBoxDimensions[0], 
                                self.boundingBoxDimensions[1])
        self.DrawText(gc)

    def RenderMainShapeHighlighting(self, gc):
        gc.SetBrush(wx.Brush('#888888', wx.TRANSPARENT))
        gc.SetPen(wx.Pen('#888888', 3, wx.DOT))
        gc.DrawRectangle(self.position[0]-3, 
                         self.position[1]-3, 
                         self.boundingBoxDimensions[0]+6, 
                         self.boundingBoxDimensions[1]+6)

    def RenderMainShapeSelection(self, gc):
        gc.SetBrush(wx.Brush('#888888', wx.TRANSPARENT))
        gc.SetPen(wx.Pen('#CC0000', 3, wx.DOT))
        gc.DrawRectangle(self.position[0]-2, 
                         self.position[1]-2, 
                         self.boundingBoxDimensions[0]+4, 
                         self.boundingBoxDimensions[1]+4)

    def DrawText(self, gc):
        gc.Clip(self.position[0], self.position[1], self.boundingBoxDimensions[0], self.boundingBoxDimensions[1])
        gc.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        gc.DrawText(self.text, self.position[0]+5, self.position[1]+5)
        gc.ResetClip()