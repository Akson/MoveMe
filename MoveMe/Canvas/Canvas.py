#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from MoveMe.Canvas.Objects.SimpleScalableTextBoxNode import SimpleScalableTextBoxNode
from MoveMe.Canvas.Factories.DefaultNodesFactory import DefaultNodesFactory
from MoveMe.Canvas.Factories.DefaultConnectionsFactory import DefaultConnectionsFactory

# Define Text Drop Target class
class TextDropTarget(wx.TextDropTarget):
    def __init__(self, canvas):
        wx.TextDropTarget.__init__(self)
        self._canvas = canvas
    
    def OnDropText(self, x, y, data):
        self._canvas.CreateNodeFromDescriptionAtPosition(data, [x, y])

class Canvas(wx.PyScrolledWindow):
    """
    Canvas stores and renders all nodes and node connections.
    It also handles all user interaction.
    """
    def __init__(self, parent, nodesFactory=DefaultNodesFactory(), connectionsFactory=DefaultConnectionsFactory(), **kwargs):
        super(Canvas, self).__init__(parent=parent)
        self.scrollStep = kwargs.get("scrollStep", 10)
        self.canvasDimensions = kwargs.get("canvasDimensions", [1600, 800])
        self.SetScrollbars(self.scrollStep, 
                           self.scrollStep, 
                           self.canvasDimensions[0]/self.scrollStep, 
                           self.canvasDimensions[1]/self.scrollStep)
        
        #This list stores all objects on canvas
        self._canvasObjects = []
        self._nodesFactory = nodesFactory
        self._connectionsFactory = connectionsFactory

        #References to objects required for implementing moving, highlighting, etc
        self._objectUnderCursor = None
        self._draggingObject = None
        self._lastDraggingPosition = None
        self._lastLeftDownPos = None
        self._selectedObject = None
        self._connectionStartObject = None

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

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
        
        self.SetDropTarget(TextDropTarget(self))

    def CreateNodeFromDescriptionAtPosition(self, nodeDescription, pos):
        node = self._nodesFactory.CreateNodeFromDescription(nodeDescription)
        if node:
            node.position = pos
            self._canvasObjects.append(node)
            self.Render()

    def Render(self):
        """Render all nodes and their connection in depth order."""
        cdc = wx.ClientDC(self)
        self.PrepareDC(cdc)
        dc = wx.BufferedDC(cdc, self._dcBuffer)
        dc.Clear()
        gc = wx.GraphicsContext.Create(dc)

        gc.SetFont(wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT))

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
            
        if self._connectionStartObject:
            gc.PushState()
            if self._objectUnderCursor and self._objectUnderCursor.connectableDestination:
                gc.SetPen(wx.Pen('#0000ff', 5, wx.DOT_DASH))
                gc.DrawLines([self._connectionStartObject.GetCenter(), self._objectUnderCursor.GetCenter()])
            else:
                gc.SetPen(wx.Pen('#ccccff', 5, wx.DOT_DASH))
                gc.DrawLines([self._connectionStartObject.GetCenter(), self._curMousePos])
            gc.PopState()


    def OnMouseMotion(self, evt):
        pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
        self._objectUnderCursor = self.FindObjectUnderPoint(pos)
        self._curMousePos = pos
        
        if not evt.LeftIsDown():
            self._draggingObject = None
            self._connectionStartObject = None

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

        if evt.ShiftDown():
            if self._objectUnderCursor.connectableSource:
                self._connectionStartObject = self._objectUnderCursor
        elif evt.ControlDown() and self._objectUnderCursor.clonable:
            text = self._objectUnderCursor.GetCloningNodeDescription()
            data = wx.TextDataObject(text)
            dropSource = wx.DropSource(self)
            dropSource.SetData(data)
            dropSource.DoDragDrop(wx.Drag_AllowMove)
        else:
            if self._objectUnderCursor.movable:
                self._lastDraggingPosition = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
                self._draggingObject = self._objectUnderCursor
        
        self._lastLeftDownPos = evt.GetPosition()

        self.Render()

    def OnMouseLeftUp(self, evt):
        if (self._connectionStartObject 
                and self._objectUnderCursor 
                and self._connectionStartObject != self._objectUnderCursor 
                and self._objectUnderCursor.connectableDestination):
            self.ConnectNodes(self._connectionStartObject, self._objectUnderCursor)

        #Selection
        if (self._lastLeftDownPos 
                and self._lastLeftDownPos[0] == evt.GetPosition()[0] 
                and self._lastLeftDownPos[1] == evt.GetPosition()[1] 
                and self._objectUnderCursor 
                and self._objectUnderCursor.selectable):
            self._selectedObject = self._objectUnderCursor
            
        self._connectionStartObject = None
        self._draggingObject = None
        self.Render()

    def FindObjectUnderPoint(self, pos):
        #Check all objects on a canvas. 
        #Some objects may have multiple components and connections.
        for obj in reversed(self._canvasObjects):
            objUnderCursor = obj.ReturnObjectUnderCursor(pos)
            if objUnderCursor: 
                return objUnderCursor
        return None

    def OnKeyPress(self, evt):
        if evt.GetKeyCode() == wx.WXK_DELETE:
            if self._selectedObject and self._selectedObject.deletable:
                self._selectedObject.Delete()
                if self._selectedObject in self._canvasObjects:
                    self._canvasObjects.remove(self._selectedObject)
                self._selectedObject = None
        else: 
            evt.Skip()

        #Update object under cursor                
        pos = self.CalcUnscrolledPosition(evt.GetPosition()).Get()
        self._objectUnderCursor = self.FindObjectUnderPoint(pos)
            
        self.Render()

    def ConnectNodes(self, source, destination):
        newConnection = self._connectionsFactory.CreateConnectionBetweenNodesFromDescription(source, destination)
        if newConnection:
            self._connectionStartObject.AddOutcomingConnection(newConnection)
            self._objectUnderCursor.AddIncomingConnection(newConnection)