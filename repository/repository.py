from storage import Storage

class Repository:
    storage: Storage = None

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

        self.storage.onInitialize.append(self.onInitialize)
        self.storage.onLoad.append(self.onLoad)
        self.storage.onSave.append(self.onSave)

    def load(self):
        self.storage.load()

    def save(self):
        self.storage.save()

    def onInitialize(self):
        pass

    def onLoad(self):
        pass

    def onSave(self):
        pass