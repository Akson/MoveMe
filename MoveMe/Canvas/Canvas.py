#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Objects.SimpleBoxNode import SimpleBoxNode

class Canvas(wx.PyScrolledWindow):
    """
    Canvas stores and renders all nodes and node connections.
    It also handles all user interaction.
    """
    def __init__(self, *args, **kw):
        super(Canvas, self).__init__(*args, **kw)
        self.scrollStep = kw.get("scrollStep", 10)
        self.canvasDimensions = kw.get("canvasDimensions", [800, 800])
        self.SetScrollbars(self.scrollStep, 
                           self.scrollStep, 
                           self.canvasDimensions[0]/self.scrollStep, 
                           self.canvasDimensions[1]/self.scrollStep)
        
        self._canvasObjects = [SimpleBoxNode([20,20]), SimpleBoxNode([140,40]), SimpleBoxNode([60,120])]

        self._dcBuffer = wx.EmptyBitmap(*self.canvasDimensions)
        self.Render()
        self.Bind(wx.EVT_PAINT, 
                  lambda evt: wx.BufferedPaintDC(self, self._dcBuffer, wx.BUFFER_VIRTUAL_AREA)
                  )

    def Render(self):
        """Render all nodes and their connection in depth order."""
        cdc = wx.ClientDC(self)
        self.PrepareDC(cdc)
        dc = wx.BufferedDC(cdc, self._dcBuffer)
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)
        
        for obj in self._canvasObjects:
            gc.PushState()
            obj.Render(gc)
            gc.PopState()
