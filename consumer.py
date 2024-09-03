from confluent_kafka import Consumer, KafkaException, KafkaError

consumer_conf = {
    'bootstrap.servers': 'localhost:9192',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)

topic = 'test_topic'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Reached end of partition
                continue
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    consumer.close()
