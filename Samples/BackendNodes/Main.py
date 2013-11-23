#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
import logging
from MoveMe.Canvas.Canvas import Canvas
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory
from MoveMe.Canvas.Objects.MessageProcessingNodes.BackendNode import SourceBackendNode,\
    BackendNode, DestinationBackendNode

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, size=[1280, 720], *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)

        supportedClasses = {
                           "SourceBackendNode":SourceBackendNode, 
                           "BackendNode":BackendNode, 
                           "DestinationBackendNode":DestinationBackendNode 
                           } 
        
        canvas = Canvas(parent=self, nodesFactory=DefaultNodesFactory(supportedClasses))
        canvas.applicationId = "BackendNode"
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "SourceBackendNode", "APPLICATION_ID": "BackendNode"}', [20,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "BackendNode", "APPLICATION_ID": "BackendNode"}', [240,20])
        canvas.CreateNodeFromDescriptionAtPosition('{"NodeClass": "DestinationBackendNode", "APPLICATION_ID": "BackendNode"}', [460,20])
        

        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe MessageProcessingGraph example")

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()