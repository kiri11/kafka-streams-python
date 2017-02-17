from kafka_streams.state import Context
from kafka_streams.processor import KafkaSource, KafkaSink


class KStreamBuilder:
    def __init__(self, config):
        self.config = config
        self.context = Context()
        self.gen = None

    def stream(self, *input_topics):
        self.gen = KafkaSource(*input_topics).gen()

    def flat_map(self, flat_mapper_gen):
        """Accepts generator and applies it to key:value pairs."""
        self.gen = flat_mapper_gen(self.gen)
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
        return self.flat_map(lambda gen: ((key, func(value)) for key, value in gen))

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

    def to_stream(self):
        return KStream

    def print(self):
        self.flat_map(lambda gen: (print("%s: %s" % (key, value)) for key, value in gen))
        return self

    def run(self):
        for x in self.gen:
            yield x

class KTable:
    pass


class KStream:
    def __init__(self, builder):
        self.gen = builder.source_gen
        self.context = builder.context

    def start(self):
        self.gen()
