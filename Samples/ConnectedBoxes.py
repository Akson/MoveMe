#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas import Canvas

class CanvasWindow(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(Canvas(self), 1, wx.EXPAND)
        self.SetSizer(s)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CanvasWindow(None).Show()
    app.MainLoop()