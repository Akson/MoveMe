#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.Base.IntermediateNode import IntermediateNode

class HubNode(IntermediateNode):
    def __init__(self, **kwargs):
        super(HubNode, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message
    
class X2Node(IntermediateNode):
    def __init__(self, **kwargs):
        super(X2Node, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message*2
    
class Plus1Node(IntermediateNode):
    def __init__(self, **kwargs):
        super(Plus1Node, self).__init__(**kwargs)
        
    def ProcessMessage(self, message):
        return message+1