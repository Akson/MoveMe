#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas
from FlowChart.FlowChartNodesFactory import FlowChartNodesFactory

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(Canvas(parent=self, nodesFactory=FlowChartNodesFactory()), 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()