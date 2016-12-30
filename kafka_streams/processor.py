from abc import ABCMeta, abstractmethod
from kafka_streams.state import LocalStateStore, StateStore
from kafka import KafkaConsumer, KafkaProducer, SimpleClient


class Processor(metaclass=ABCMeta):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def process(self):
        pass

    def punctuate(self):
        ...


class Source:
    def __init__(self, context, name):
        self.offset_store = context.put(name, LocalStateStore)

    def process_gen(self):
        """Must save its offset to state store"""
        pass


class KafkaSource(Source):
    pass


class KafkaSink(Processor):
    def __init__(self, context):
        super().__init__(context)

    def process(self):
        ...
