import pickle
import os

FILE_DATA = "data.dat"

class Storage:
    data = {}

    onInitialize = []
    onLoad = []
    onSave = []

    def load(self):
        if not os.path.isfile('data.dat'):
            for x in self.onInitialize:
                x()

            self.save()

        with open(FILE_DATA, 'rb') as file:
            self.data = pickle.load(file)

            for x in self.onLoad:
                x()

    def save(self):
        with open(FILE_DATA, 'wb') as file:
            for x in self.onSave:
                x()

            pickle.dump(self.data, file)