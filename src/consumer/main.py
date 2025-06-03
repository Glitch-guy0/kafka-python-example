from kafka import KafkaConsumer
import time

try:
    consumer = KafkaConsumer(
        'help1',  # Specify the topic to consume
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        heartbeat_interval_ms=  10000,
        session_timeout_ms=30000,
        consumer_timeout_ms=30000,
        value_deserializer=lambda x: x.decode('utf-8'),
        key_deserializer=lambda x: x.decode('utf-8') if x else None,
    )

    if consumer.bootstrap_connected():
        print("connected to server")

    # consumer.subscribe(topics=['help1'])
    while not consumer.assignment():
        print("Waiting for partition assignment...")
        time.sleep(2)


    while True:
        for message in consumer.poll(timeout_ms=1000).values():
            for record in message:
                print(f"Received message: {record.value.decode('utf-8')}")
        time.sleep(2)

    consumer.close()
except Exception as e:
    print(f"Error in Kafka consumer: {e}")