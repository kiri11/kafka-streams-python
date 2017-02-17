from abc import ABCMeta, abstractmethod
import os
import json


class StateStore(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.storage = self.load() or {}

    @abstractmethod
    def load(self):
        pass

    def get(self, key):
        return self.storage.get(key)

    def __setitem__(self, key, value):
        self.storage[key] = value
        return key

    @abstractmethod
    def save(self):
        pass


class Context:
    def __init__(self):
        self.stores = {}

    def put(self, state_store: StateStore):
        self.stores[state_store.name] = state_store

    def load(self):
        for store in self.stores:
            store.load()

    def save(self):
        for store in self.stores:
            store.save()


class LocalStateStore(StateStore):
    """StateStore implementation using
    local file and json serialization.
    """

    def __init__(self, name):
        self.filename = name + ".json"
        super().__init__(name)

    def load(self):
        if os.path.isfile(self.filename):
            with open(self.filename):
                return json.load(self.filename)

    def save(self):
        with(open(self.filename, 'w')) as f:
            json.dump(self.storage, f)
