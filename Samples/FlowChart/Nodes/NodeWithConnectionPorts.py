#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import wx
from FlowChart.Nodes.ConnectionPort import ConnectionPort
from MoveMe.Canvas.Objects.Base.CanvasObject import CanvasObject
from MoveMe.Canvas.Objects.Base.ClonableObject import ClonableObject
from MoveMe.Canvas.Objects.Base.DeletableObject import DeletableObject
from MoveMe.Canvas.Objects.Base.MovableObject import MovableObject
from MoveMe.Canvas.Objects.Base.SelectableObject import SelectableObject

class NodeWith4ConnectionPorts(ClonableObject, DeletableObject, SelectableObject, MovableObject, CanvasObject):
    def __init__(self, **kwargs):
        super(NodeWith4ConnectionPorts, self).__init__(**kwargs)

        self._connectionPorts = [ConnectionPort(self), ConnectionPort(self), ConnectionPort(self), ConnectionPort(self)]

    def Render(self, gc):
        self.RenderMainShape(gc)
        
        self.UpdateConnectionPortsPositions()
        for connectionPort in self._connectionPorts:
            connectionPort.Render(gc)

    def RenderHighlighting(self, gc):
        self.RenderMainShapeHighlighting(gc)

        self.UpdateConnectionPortsPositions()
        for connectionPort in self._connectionPorts:
            connectionPort.RenderBox(gc)

    def RenderSelection(self, gc):
        self.RenderMainShapeSelection(gc)

    def ReturnObjectUnderCursor(self, pos):
        for connectionPort in self._connectionPorts:
            connectionComponent = connectionPort.ReturnObjectUnderCursor(pos)
            if connectionComponent: 
                return connectionComponent

        if self.IsPointInside(pos): 
            return self
        
        return None

    def Delete(self):
        for connectionPort in self._connectionPorts:
            connectionPort.Delete()


    def IsPointInside(self, pos):
        raise NotImplementedError()
    
    def UpdateConnectionPortsPositions(self):
        raise NotImplementedError()

    def RenderMainShape(self, gc):
        raise NotImplementedError()

    def RenderMainShapeHighlighting(self, gc):
        raise NotImplementedError()

    def RenderMainShapeSelection(self, gc):
        raise NotImplementedError()

    def GetListOfAllPossibleConnectionsSources(self):
        return self._connectionPorts
    
    def SaveObjectToDict(self):
        nodeDict = {"NodeClass":self.__class__.__name__}
        nodeDict["NodeParameters"] = {}
        for key in self.__dict__:
            if key[0]!='_':
                nodeDict["NodeParameters"][key] = self.__dict__[key]
        nodeDict["_ConnectionPorts"] = [] 
        for connectionPort in self._connectionPorts:
            nodeDict["_ConnectionPorts"].append(connectionPort.SaveObjectToDict())
        return nodeDict
    
    def LoadObjectFromDict(self, parametersDict):
        for key in parametersDict:
            if key[0]!='_':
                self.__dict__[key] = parametersDict[key] 

        if "_ConnectionPorts" in parametersDict:
            for connectionPortDict in parametersDict["_ConnectionPorts"]:
                self._connectionPorts.LoadObjectFromDict(connectionPortDict)