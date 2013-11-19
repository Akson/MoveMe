#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
from MessageProcessingGraph.Nodes.SourceNode import SourceNode
from MessageProcessingGraph.Nodes.IntermediateNode import IntermediateNode
from MessageProcessingGraph.Nodes.DestinationNode import DestinationNode
import json

class NodesFactory(NodesFactoryInterface):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        print nodeDescription
        nodeDescriptionDict = json.loads(nodeDescription)
        nodeClasses = {"SourceNode":SourceNode, "IntermediateNode":IntermediateNode, "DestinationNode":DestinationNode}
        nodeClass = nodeClasses[nodeDescriptionDict["NodeClass"]]
        node = nodeClass()
        node.__dict__.update(nodeDescriptionDict["NodeParameters"])
        return node