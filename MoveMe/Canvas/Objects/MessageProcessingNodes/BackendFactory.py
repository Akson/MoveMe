#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)
import importlib

def CreateBackendFromPath(parentNode, backendPath, backendParameters={}):
    if backendPath == None:
        return None
    
    moduleName = ".".join(backendPath.split(".")[:-1])
    backendModule = importlib.import_module(moduleName)
    
    className = backendPath.split(".")[-1]
    backendClass = getattr(backendModule, className)
    
    backendObj = backendClass(parentNode)
    backendObj.SetParameters(backendParameters)

    return backendObj