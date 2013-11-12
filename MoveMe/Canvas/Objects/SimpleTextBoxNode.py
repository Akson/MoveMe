#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.SimpleBoxNode import SimpleBoxNode

class SimpleTextBoxNode(SimpleBoxNode):
    def __init__(self, **kwargs):
        super(SimpleTextBoxNode, self).__init__(**kwargs)
        self.text = kwargs.get("text", "No text")
        
    def Render(self, gc):
        super(SimpleTextBoxNode, self).Render(gc)

        gc.DrawText(self.text, self.position[0]+10, self.position[1]+10)
        
    def GetCloningNodeDescription(self):
        return self.text