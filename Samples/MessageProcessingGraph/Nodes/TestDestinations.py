#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.Base.DestinationNode import DestinationNode

class Message2ConsoleWriterNode(DestinationNode):
    def __init__(self):
        super(Message2ConsoleWriterNode, self).__init__()
        
    def ReceiveMessage(self, message):
        print "Destination", message