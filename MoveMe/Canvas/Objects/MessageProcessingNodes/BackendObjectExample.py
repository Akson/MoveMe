#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)

class PassThroughBackendObject(object):
    def __init__(self, parentNode):
        self._parentNode = parentNode
    
    def GetParameters(self):
        """
        Returns a dictionary with object parameters, their values, 
        limits and ways to change them.
        """
        return {}
    
    def SetParameters(self, parameters):
        """
        Gets a dictionary with parameter values and
        update object parameters accordingly
        """
        pass
    
    def ProcessMessage(self, message):
        """
        This message is called when a new message comes. 
        If an incoming message should be processed by following nodes, the 
        'self._parentNode.SendMessage(message)'
        should be called with an appropriate message.
        """
        self._parentNode.SendMessage(message)