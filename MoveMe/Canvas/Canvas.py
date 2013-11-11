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
        self._canvasObjects = [SimpleBoxNode(position=[20,20]), SimpleBoxNode(position=[140,40]), SimpleBoxNode(position=[60,120])]

        #References to objects required for implementing moving, highlighting, etc
        self._objectUnderCursor = None
        self._draggingObject = None
        self._lastDraggingPosition = None
        self._lastLeftDownPos = None
        self._selectedObject = None

        #Rendering initialization
        self._dcBuffer = wx.EmptyBitmap(*self.canvasDimensions)
        self.Render()
        self.Bind(wx.EVT_PAINT, 
                  lambda evt: wx.BufferedPaintDC(self, self._dcBuffer, wx.BUFFER_VIRTUAL_AREA)
                  )
        
        #User interaction handling
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

        if self._selectedObject:
            gc.PushState()
            self._selectedObject.RenderSelection(gc)
            gc.PopState()

    def OnMouseMotion(self, evt):
        pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
        self._objectUnderCursor = self.FindObjectUnderPoint(pos)
        
        if not evt.LeftIsDown():
            self._draggingObject = None

        if evt.LeftIsDown() and evt.Dragging() and self._draggingObject:
            dx = pos[0]-self._lastDraggingPosition[0]
            dy = pos[1]-self._lastDraggingPosition[1]
            newX = self._draggingObject.position[0]+dx
            newY = self._draggingObject.position[1]+dy
            
            #Check canvas boundaries 
            newX = min(newX, self.canvasDimensions[0]-self._draggingObject.boundingBoxDimensions[0])
            newY = min(newY, self.canvasDimensions[1]-self._draggingObject.boundingBoxDimensions[1])
            newX = max(newX, 0)
            newY = max(newY, 0)
            
            self._draggingObject.position = [newX, newY]

            #Cursor will be at a border of a node if it goes out of canvas
            self._lastDraggingPosition = [min(pos[0], self.canvasDimensions[0]), min(pos[1], self.canvasDimensions[1])]
        
        self.Render()

    def OnMouseLeftDown(self, evt):
        if not self._objectUnderCursor:
            return

        if self._objectUnderCursor.movable:
            self._lastDraggingPosition = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
            self._draggingObject = self._objectUnderCursor
        
        self._lastLeftDownPos = evt.GetPosition()

        self.Render()

    def OnMouseLeftUp(self, evt):
        #Selection
        if (self._lastLeftDownPos 
                and self._lastLeftDownPos[0] == evt.GetPosition()[0] 
                and self._lastLeftDownPos[1] == evt.GetPosition()[1] 
                and self._objectUnderCursor 
                and self._objectUnderCursor.selectable):
            self._selectedObject = self._objectUnderCursor
            
        self.Render()

    def FindObjectUnderPoint(self, pos):
        #Check all objects on a canvas. 
        #Some objects may have multiple components and connections.
        for obj in reversed(self._canvasObjects):
            objUnderCursor = obj.ReturnObjectUnderCursor(pos)
            if objUnderCursor: 
                return objUnderCursor
        return None
