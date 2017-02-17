from abc import ABCMeta, abstractmethod
import msgpack
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


class KafkaSource:
    def __init__(self, *input_topics, key_deserializer=None, value_deserializer=None):
        """Source is a processor with no input."""
        self.key_deserializer = key_deserializer
        self.value_deserializer = value_deserializer
        self.consumer = KafkaConsumer(*input_topics,
                                      bootstrap_servers=['kafka:9092'],
                                      auto_offset_reset='earliest',
                                      group_id=None,
                                      enable_auto_commit=False,
                                      consumer_timeout_ms=1000,
                                      value_deserializer=msgpack.loads
                                      )

    def gen(self):
        for msg in self.consumer:
            yield msg.value


class KafkaSink(Processor):
    def __init__(self, context):
        super().__init__(context)

    def process(self):
        ...
