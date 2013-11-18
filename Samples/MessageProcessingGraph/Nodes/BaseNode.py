#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.SimpleBoxNode import SimpleBoxNode
import wx
from MoveMe.Canvas.Objects.Base.ObjectWithText import ObjectWithText

class BaseNode(ObjectWithText, SimpleBoxNode):
    def __init__(self, **kwargs):
        super(BaseNode, self).__init__(**kwargs)

    def Render(self, gc):
        super(BaseNode, self).Render(gc)
        self.DrawText(gc)
    
    def DrawText(self, gc):
        gc.Clip(self.position[0], self.position[1], self.boundingBoxDimensions[0], self.boundingBoxDimensions[1])
        gc.SetFont(wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        gc.DrawText(self.text, self.position[0]+5, self.position[1]+5)
        
    def GetCloningNodeDescription(self):
        return self.text