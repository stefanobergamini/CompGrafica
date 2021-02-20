class Objects:
    listObjects = []
    selectObject = None

    @staticmethod
    def clearObjects(object):
        Objects.listObjects = []

    @staticmethod
    def addObject(object):
        Objects.listObjects.append(object)

    @staticmethod
    def selectObject(object):
        Objects.selectObject = object
        print(Objects.selectObject)

    @staticmethod
    def clearSelectObject():
        Objects.selectObject = None
