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
        
        #This list stores all objects on canvas
        self._canvasObjects = [SimpleBoxNode([20,20]), SimpleBoxNode([140,40]), SimpleBoxNode([60,120])]

        #References to objects required for implementing various operations
        self._objectUnderCursor = None

        #Rendering initialization
        self._dcBuffer = wx.EmptyBitmap(*self.canvasDimensions)
        self.Render()
        self.Bind(wx.EVT_PAINT, 
                  lambda evt: wx.BufferedPaintDC(self, self._dcBuffer, wx.BUFFER_VIRTUAL_AREA)
                  )
        
        self.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)

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

        if self._objectUnderCursor:
            gc.PushState()
            self._objectUnderCursor.RenderHighlighting(gc)
            gc.PopState()

    def OnMouseMotion(self, evt):
        pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
        self._objectUnderCursor = self.FindObjectUnderPoint(pos)
        self.Render()

    def OnMouseLeftDown(self, evt):
        pass
    def OnMouseLeftUp(self, evt):
        pass

    def FindObjectUnderPoint(self, pos):
        #Check all objects on a canvas. Some objects may have multiple components and connections.
        for obj in reversed(self._canvasObjects):
            objUnderCursor = obj.ReturnObjectUnderCursor(pos)
            if objUnderCursor: 
                return objUnderCursor
        return None
