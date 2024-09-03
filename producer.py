from confluent_kafka import Producer

producer_conf = {
    'bootstrap.servers': 'localhost:9192'
}

producer = Producer(producer_conf)

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

topic = 'test_topic'
for i in range(10):
    producer.produce(topic, key=str(i), value=f"Message {i}", callback=acked)
    producer.poll(1)

producer.flush()
