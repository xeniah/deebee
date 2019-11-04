class TableNoIndex:
    def __init__(self):
        self.records = []

    def insert(self, record):
        self.records.append(record)
        return len(self.records)

    def getById(self, id):
        if id < len(self.records):
            return self.records[id-1]
        else:
            raise

    def getByAttribute(self, attribute, value):
        return [record for record in self.records if record[attribute] == value]
        #return list(filter(lambda r: r[attribute] == value, self.records))
