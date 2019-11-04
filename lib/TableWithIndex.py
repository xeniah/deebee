class TableWithIndex:
    def __init__(self):
        self.records = []
        self.indices = {
            # attributeName: {  "value1": [ids ...], "value2": [ids ...] }
        }

    def createIndex(self, attribute):
        self.indices[attribute] = {}

    def updateIndex(self, attribute, value, id):

        entry = self.indices[attribute]

        if value in entry:
            entry[value] += [id]
        else:
            entry[value] = [id]

    def insert(self, record):
        self.records.append(record)
        id = len(self.records)
        for attrib in record.keys():
            if attrib in self.indices.keys():
                self.updateIndex(attrib, record[attrib], id)
        return id

    def getById(self, id):
        if id < len(self.records):
            return self.records[id-1]
        else:
            return None

    def getByAttribute(self, attribute, value):
        if attribute in self.indices and value in self.indices[attribute]:
            ids = self.indices[attribute][value]
            return ids #[self.records[i-1] for i in ids ]
        else:
            return [record for record in self.records if record[attribute] == value]


