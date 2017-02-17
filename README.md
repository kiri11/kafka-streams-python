# kafka-streams-python
KafkaStreams library in Python.

Reasons for such a library outlined in 
[this great article](https://www.confluent.io/blog/introducing-kafka-streams-stream-processing-made-simple/).
However, it's only implemented in Java and there is [no plans](https://github.com/confluentinc/confluent-kafka-python/issues/38)
to support other languages by Confluence. This is an opportunity for the community to step up and provide a solution.

This is NOT an exact implementation of Java KafkaStreams API, but more of a library based on KafkaStreams DSL 
to make stream processing more pythonic.

[Concepts](http://docs.confluent.io/3.0.0/streams/concepts.html) are  mostly the same as in Java KafkaStreams library.

### Initial goals:
 - Provide a convenient interface for creating stream processing topologies.
 - Allow explicit state management.
 - Ensure saving intermediate state even in case of unexpected failure.
 
 ### Stretch goals:
 - Rebalancing
 - Window management
 - Better fault tolerance
 - Asynchronous execution
 