#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.Base.IntermediateNode import IntermediateNode

class Hub(IntermediateNode):
    def __init__(self, **kwargs):
        super(Hub, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message
    
class X2(IntermediateNode):
    def __init__(self, **kwargs):
        super(X2, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message*2
    
class Plus1(IntermediateNode):
    def __init__(self, **kwargs):
        super(Plus1, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message+1