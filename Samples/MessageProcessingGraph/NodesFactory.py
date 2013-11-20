#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
import json
from Samples import MessageProcessingGraph
from MessageProcessingGraph.Nodes.Base.SourceNode import SourceNode
from MessageProcessingGraph.Nodes.Base.IntermediateNode import IntermediateNode
from MessageProcessingGraph.Nodes.Base.DestinationNode import DestinationNode
from MessageProcessingGraph.Nodes.TestSources import *
from MessageProcessingGraph.Nodes.TestDestinations import *
from MessageProcessingGraph.Nodes.TestIntermediates import *

class NodesFactory(NodesFactoryInterface):
    def __init__(self):
        pass
    
    def CreateNodeFromDescription(self, nodeDescription):
        print nodeDescription
        nodeDescriptionDict = json.loads(nodeDescription)
        if ("APPLICATION_ID" in nodeDescriptionDict 
            and nodeDescriptionDict["APPLICATION_ID"] != MessageProcessingGraph.APPLICATION_ID):
            return None
        
        nodeClasses = {
                       "NumbersSequenceSource":NumbersSequenceSource, 
                       "Hub":Hub, 
                       "X2":X2, 
                       "Plus1":Plus1, 
                       "Message2ConsoleWriterNode":Message2ConsoleWriterNode
                       }
        nodeClass = nodeClasses[nodeDescriptionDict["NodeClass"]]
        node = nodeClass()
        node.__dict__.update(nodeDescriptionDict["NodeParameters"])
        return node