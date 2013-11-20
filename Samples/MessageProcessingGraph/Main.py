#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
import logging
from MoveMe.Canvas.Canvas import Canvas
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory
from MessageProcessingGraph.Nodes.TestSources import NumbersSequenceSource
from MessageProcessingGraph.Nodes.TestIntermediates import Hub, X2, Plus1
from MessageProcessingGraph.Nodes.TestDestinations import Message2ConsoleWriterNode

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, size=[1280, 720], *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)

        supportedClasses = {
                           "NumbersSequenceSource":NumbersSequenceSource, 
                           "Hub":Hub, 
                           "X2":X2, 
                           "Plus1":Plus1, 
                           "Message2ConsoleWriterNode":Message2ConsoleWriterNode
                           } 
        
        canvas = Canvas(parent=self, nodesFactory=DefaultNodesFactory(supportedClasses))
        canvas.applicationId = "MessageProcessingGraph"
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "NumbersSequenceSource", "APPLICATION_ID": "MessageProcessingGraph"}', [20,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "Hub", "APPLICATION_ID": "MessageProcessingGraph"}', [240,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "X2", "APPLICATION_ID": "MessageProcessingGraph"}', [240,100])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "Plus1", "APPLICATION_ID": "MessageProcessingGraph"}', [240,180])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "Message2ConsoleWriterNode", "APPLICATION_ID": "MessageProcessingGraph"}', [460,20])

        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe MessageProcessingGraph example")

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()