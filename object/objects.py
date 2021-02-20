class Objects:
    listObjects = []
    selectedObject = None
    numberObjects = 1

    @staticmethod
    def clearObjects(object):
        Objects.listObjects = []

    @staticmethod
    def addObject(object):
        Objects.listObjects.append(object)
        Objects.numberObjects += 1

    @staticmethod
    def selectObject(objectLabel):
        for object in Objects.listObjects:
            if (object.label == objectLabel):
                Objects.selectedObject = object
                break

    @staticmethod
    def clearSelectObject():
        Objects.selectedObject = None
