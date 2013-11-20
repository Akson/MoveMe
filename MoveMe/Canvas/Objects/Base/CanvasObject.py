#Created by Dmytro Konobrytskyi, 2013 (github.com/Akson/MoveMe)

class ObjectIDGenerator(object):
    _currentId = 0
    @staticmethod
    def GetNextId():
        resultId = ObjectIDGenerator._currentId
        ObjectIDGenerator._currentId+=1
        return resultId

class CanvasObject(object):
    def __init__(self):
        self.id = ObjectIDGenerator.GetNextId()
        #Supported operations
        self.clonable = False
        self.movable = False
        self.deletable = False
        self.selectable = False
        self.connectableSource = False
        self.connectableDestination = False
        
    def Render(self, gc): 
        """
        Rendering method should draw an object.
        gc: GraphicsContext object that should be used for drawing.
        """
        raise NotImplementedError()
    
    def RenderHighlighting(self, gc):
        """
        RenderHighlighting method should draw an object 
        with a highlighting border around it.
        gc: GraphicsContext object that should be used for drawing.
        """ 
        raise NotImplementedError()

    def ReturnObjectUnderCursor(self, pos):
        """
        ReturnObjectUnderCursor method returns a top component 
        of this object at a given position or None if position 
        is outside of all objects.
        pos: tested position as a list of x, y coordinates such as [100, 200]
        """
        raise NotImplementedError()