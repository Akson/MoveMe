#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.MessageProcessingNodes.Base import BaseMessageProcessingNode
from MoveMe.Canvas.Objects.MessageProcessingNodes.BackendFactory import CreateBackendFromPath
import wx
import os.path
import logging
import sys
import traceback

class BackendNode(BaseMessageProcessingNode):
    def __init__(self):
        super(BackendNode, self).__init__()
        
        self.backendPath = None
        self._backendObject = None
        self.parametersForCloning.append("backendPath")
        BackendNode.shortHumanFriendlyDescription = "Message processing node with backend"

    def SetBackend(self, backendPath, backendParameters = {}):
        self._backendObject = CreateBackendFromPath(self, backendPath, backendParameters)
        if self._backendObject:
            self.backendPath = backendPath
            
    def ReloadBackend(self):
        if self._backendObject:
            parameters = self._backendObject.GetParameters()
            self._backendObject.Delete()
            self._backendObject = CreateBackendFromPath(self, self.backendPath, parameters)
    
    def SendMessage(self, message):
        if not self.connectableSource:
            return

        for connection in self.GetOutcomingConnections():
                connection.destination.ReceiveMessage(message)
    
    def ReceiveMessage(self, message):
        if not self.connectableDestination:
            return
        
        if self._backendObject == None:
            return
        
        try:
            self._backendObject.ProcessMessage(message)
        except:
            print traceback.format_exc()
        
    def SaveObjectToDict(self):
        nodeDict = {"NodeClass":self.__class__.__name__}
        nodeParameters = self.GetCloningNodeDescription()["NodeParameters"]
        nodeParameters["position"] = self.position
        nodeParameters["backendParameters"] = self._backendObject.GetParameters() if self._backendObject else {} 
        nodeDict["NodeParameters"] = nodeParameters 
        return nodeDict
    
    def LoadObjectFromDict(self, parametersDict):
        for key in self.parametersForCloning:
            if key in  parametersDict:
                self.__dict__[key] = parametersDict[key]
        if "position" in parametersDict:
            self.position = parametersDict["position"]
        self.SetBackend(parametersDict["backendPath"], parametersDict.get("backendParameters", {}))

    def Delete(self):
        if self._backendObject:
            self._backendObject.Delete()
            
    def AppendContextMenuItems(self, menu):
        item = wx.MenuItem(menu, wx.NewId(), "Select backend")
        menu.Bind(wx.EVT_MENU, self.OnSelectBackend, item)
        menu.AppendItem(item)

        if self._backendObject:
            item = wx.MenuItem(menu, wx.NewId(), "Reload backend")
            menu.Bind(wx.EVT_MENU, (lambda evt: self.ReloadBackend()) , item)
            menu.AppendItem(item)
        
        if self._backendObject:
            menu.AppendSeparator()
            self._backendObject.AppendContextMenuItems(menu)

    def OnSelectBackend(self, event):
        dlg = wx.FileDialog(None, "Select a Python module with a Backend class", '', "", "Python modules (*.py)|*.py", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filePath = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
            classPath = self.GetClassPythFromFilePath(filePath)
            if classPath:
                self.SetBackend(classPath)
            else:
                logging.error("Cannot create backend object. Probably backend class is not in PythonPath")
                
        dlg.Destroy()
        
    def GetClassPythFromFilePath(self, filePath):
        pythonPaths = sys.path
        for path in pythonPaths:
            if filePath.find(path) == 0:
                classPath = ".".join(filePath[len(path)+1:-3].split('\\'))
                return classPath
        return None

            
class SourceBackendNode(BackendNode):
    def __init__(self):
        super(SourceBackendNode, self).__init__()
        self.connectableDestination = False
        self.nodeBackgroundColor = '#DDFFDD'
        SourceBackendNode.shortHumanFriendlyDescription = "Message source node with backend"


class DestinationBackendNode(BackendNode):
    def __init__(self):
        super(DestinationBackendNode, self).__init__()
        self.connectableSource = False
        self.nodeBackgroundColor = '#FFDDDD'
        DestinationBackendNode.shortHumanFriendlyDescription = "Message destination node with backend"

