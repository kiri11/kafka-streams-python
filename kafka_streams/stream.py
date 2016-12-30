from kafka_streams.state import Context
from kafka_streams.processor import Source, KafkaSink


class KafkaStream:
    def __init__(self, config, source: Source):
        self.config = config
        self.context = Context()
        self.source_gen = source.process_gen
        self.pipe = []

    def flat_map(self, flat_mapper_gen):
        """Accepts generator and applies it to key:value pairs."""
        self.source_gen = flat_mapper_gen(self.source_gen)
        return self

    def process(self, processor, *args):
        """Accepts processor instance. Use for stateful processing."""
        self.map(processor(self.context).process)
        return self

    def filter(self, predicate):
        ...
        return self

    def map(self, func):
        return self.flat_map(lambda gen: (func(key, value) for key, value in gen))

    def map_values(self, func):
        return self.flat_map(lambda gen: (key, func(value) for key, value in gen))

    def select_key(self):
        ...
        return self

    def flat_map_values(self):
        ...
        return self

    def branch(self):
        ...

    def to(self, sink_topic):
        self.process(KafkaSink, sink_topic)


class KTable(KafkaStream):
    pass


class KStream(KafkaStream):
    pass

