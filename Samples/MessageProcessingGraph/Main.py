#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas
from MessageProcessingGraph.NodesFactory import NodesFactory
import logging

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, size=[1280, 720], *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)

        canvas = Canvas(parent=self, nodesFactory=NodesFactory())
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