#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import importlib

def CreateBackendFromPath(parentNode, backendPath, backendParameters={}):
    if backendPath == None:
        return None
    
    backendModule = importlib.import_module(backendPath)
    reload(backendModule)
    backendClass = getattr(backendModule, "Backend")
    
    backendObj = backendClass(parentNode)
    backendObj.SetParameters(backendParameters)

    return backendObj