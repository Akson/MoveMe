#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Factories.NodesFactoryInterface import NodesFactoryInterface
from MessageProcessingGraph.Nodes.Base.SourceNode import SourceNode
from MessageProcessingGraph.Nodes.Base.IntermediateNode import IntermediateNode
from MessageProcessingGraph.Nodes.Base.DestinationNode import DestinationNode
from MessageProcessingGraph.Nodes.TestSources import *
from MessageProcessingGraph.Nodes.TestDestinations import *
from MessageProcessingGraph.Nodes.TestIntermediates import *
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory

class NodesFactory(DefaultNodesFactory):
    def __init__(self):
        supportedClasses = {
                           "NumbersSequenceSource":NumbersSequenceSource, 
                           "Hub":Hub, 
                           "X2":X2, 
                           "Plus1":Plus1, 
                           "Message2ConsoleWriterNode":Message2ConsoleWriterNode
                           } 
        super(NodesFactory, self).__init__(supportedClasses)