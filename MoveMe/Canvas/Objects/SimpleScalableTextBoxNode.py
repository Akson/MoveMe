#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.SimpleBoxNode import SimpleBoxNode
from MoveMe.Canvas.Objects.Base.ObjectWithText import ObjectWithText

class SimpleScalableTextBoxNode(ObjectWithText, SimpleBoxNode):
    def __init__(self, **kwargs):
        super(SimpleScalableTextBoxNode, self).__init__(**kwargs)
        self.parametersForCloning.append("text")
        
    def Render(self, gc):
        textDimensions = gc.GetTextExtent(self.text)
        self.boundingBoxDimensions = [textDimensions[0]+20, textDimensions[1]+20] 
        super(SimpleScalableTextBoxNode, self).Render(gc)

        gc.DrawText(self.text, self.position[0]+10, self.position[1]+10)
