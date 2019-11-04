class Table:
    def __init__(self):
        self.storage = []
        self.indices = {}
    
    def insert(self, obj):
        self.storage.append(obj)
        
        id = len(self.storage)
        for obj_attrib in obj.keys():
            if obj_attrib in self.indices.keys():
                index = self.indices[obj_attrib]
                val = obj[obj_attrib]
                index[val] = index.get(val, []) + [id]
           
        return len(self.storage)
    
    def updateIndex(self, attribute, value, id):
        index = self.indices.get(attribute, [])
        ids = index[value]
        
        index[value] = index.get(value, []) + [id]
    
    def createIndex(self, attribute):
        self.indices[attribute] = {}
    
    def getById(self, id):
        if 0 < id <= len(self.storage):
            return self.storage[id-1]
        else:
            return None
    
    def findBy(self, attribute, value):
        if attribute in self.indices.keys():
            index = self.indices[attribute]
            ids = index.get(value, [])
            return [self.getById(id) for id in ids]
        
        return [k for k in self.storage if k[attribute] == value]
    