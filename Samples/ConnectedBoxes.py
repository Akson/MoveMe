#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas
import logging
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory
from MoveMe.Canvas.Objects.SimpleScalableTextBoxNode import SimpleScalableTextBoxNode

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)
        
        supportedClasses = {
                            "SimpleScalableTextBoxNode":SimpleScalableTextBoxNode
                            }
        
        canvas = Canvas(parent=self, nodesFactory=DefaultNodesFactory(supportedClasses))
        canvas.applicationId = "ConnectedBoxes"
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "SimpleScalableTextBoxNode", "APPLICATION_ID": "ConnectedBoxes", "NodeParameters":{"text":"A"}}', [20,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "SimpleScalableTextBoxNode", "APPLICATION_ID": "ConnectedBoxes", "NodeParameters":{"text":"B"}}', [140,40])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "SimpleScalableTextBoxNode", "APPLICATION_ID": "ConnectedBoxes", "NodeParameters":{"text":"C"}}', [60,120])
                               
        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe ConnectedBoxes example")

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()