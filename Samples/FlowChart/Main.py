#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas
from FlowChart.FlowChartNodesFactory import FlowChartNodesFactory
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory
from FlowChart.Nodes.BoxNode import BoxNode
import logging

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)

        supportedClasses = {
                            "BoxNode":BoxNode
                            }
        
        canvas = Canvas(parent=self, nodesFactory=DefaultNodesFactory(supportedClasses))
        canvas.applicationId = "FlowChart"

        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "BoxNode", "APPLICATION_ID": "FlowChart", "NodeParameters":{"text":"A"}}', [20,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "BoxNode", "APPLICATION_ID": "FlowChart", "NodeParameters":{"text":"B"}}', [140,40])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "BoxNode", "APPLICATION_ID": "FlowChart", "NodeParameters":{"text":"C"}}', [60,120])

        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe FlowChart example")

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()