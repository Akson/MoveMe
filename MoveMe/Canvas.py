#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx

class Canvas(wx.PyScrolledWindow):
    """
    Canvas stores and renders all nodes and node connections.
    It also handles all user interaction.
    """
    def __init__(self, *args, **kw):
        super(Canvas, self).__init__(*args, **kw)
        self.scrollStep = kw.get("scrollStep", 10)
        self.canvasDimensions = kw.get("canvasDimensions", [800, 800])
        self.SetScrollbars(self.scrollStep, self.scrollStep, self.canvasDimensions[0]/self.scrollStep, self.canvasDimensions[1]/self.scrollStep)

        self._dcBuffer = wx.EmptyBitmap(*self.canvasDimensions)
        self.Render()
        self.Bind(wx.EVT_PAINT, lambda evt: wx.BufferedPaintDC(self, self._dcBuffer, wx.BUFFER_VIRTUAL_AREA))

    def Render(self):
        cdc = wx.ClientDC(self)
        self.PrepareDC(cdc)
        dc = wx.BufferedDC(cdc, self._dcBuffer)
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)
        
        gc.SetPen(wx.Pen('#000000', 2, wx.SOLID))
        gc.DrawRoundedRectangle(12, 34, 56, 78, 10)
        gc.DrawRoundedRectangle(112, 134, 156, 178, 10)
