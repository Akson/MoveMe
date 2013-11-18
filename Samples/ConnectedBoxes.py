#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Canvas import Canvas

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)
        
        canvas = Canvas(parent=self)
        canvas.CreateNodeFromDescriptionAtPosition("A", [20,20])
        canvas.CreateNodeFromDescriptionAtPosition("B", [140,40])
        canvas.CreateNodeFromDescriptionAtPosition("C", [60,120])
                               
        s.Add(canvas, 1, wx.EXPAND)
        self.SetSizer(s)
        self.SetTitle("MoveMe")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()