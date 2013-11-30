#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
from MoveMe.Canvas.Objects.MessageProcessingNodes.Base import BaseMessageProcessingNode
from MoveMe.Canvas.Objects.MessageProcessingNodes.BackendFactory import CreateBackendFromPath

class BackendNode(BaseMessageProcessingNode):
    def __init__(self):
        super(BackendNode, self).__init__()
        
        self.backendPath = None
        self._backendObject = None
        self.parametersForCloning.append("backendPath")
        BackendNode.shortHumanFriendlyDescription = "Message processing node with backend"

    def SetBackend(self, backendPath, backendParameters = {}):
        self.backendPath = backendPath
        self._backendObject = CreateBackendFromPath(self, backendPath, backendParameters)
    
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
        
        self._backendObject.ProcessMessage(message)
        
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

