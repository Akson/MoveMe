#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas
from MessageProcessingGraph.NodesFactory import NodesFactory

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)

        canvas = Canvas(parent=self, nodesFactory=NodesFactory())
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "NumbersSequenceSource", "NodeParameters": {}}', [20,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "HubNode", "NodeParameters": {}}', [140,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "X2Node", "NodeParameters": {}}', [140,60])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "Plus1Node", "NodeParameters": {}}', [140,100])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "Message2ConsoleWriterNode", "NodeParameters": {}}', [260,20])

        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()