#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MessageProcessingGraph.Nodes.Base.SourceNode import SourceNode
import time
import thread

class TimingBasedSourceNode(SourceNode):
    nodesList = None
    def __init__(self, **kwargs):
        super(TimingBasedSourceNode, self).__init__(**kwargs)
        if TimingBasedSourceNode.nodesList == None:
            TimingBasedSourceNode.nodesList = []
            thread.start_new_thread(self.SourcesThreadFunction, ())
    
    @staticmethod
    def SourcesThreadFunction():
        while True:
            for node in TimingBasedSourceNode.nodesList:
                node.PerformMessageSending()
            time.sleep(1)
            print "===================================="
            
    def PerformMessageSending(self):
        raise NotImplementedError()

class NumbersSequenceSource(TimingBasedSourceNode):
    def __init__(self, **kwargs):
        super(NumbersSequenceSource, self).__init__(**kwargs)
        
        self.value = self.id
        TimingBasedSourceNode.nodesList.append(self)
    
    def PerformMessageSending(self):
        message = self.value
        self.value += 1
        print "Source", message
        self.SendMessage(message)