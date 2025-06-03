from kafka import KafkaConsumer

try:
    consumer = KafkaConsumer(
        'help1',
        bootstrap_servers='localhost:9092',
        max_poll_records = 100,
        value_deserializer=lambda x: x.decode('ascii'),
        auto_offset_reset='earliest'#,'smallest'
    )

    if not consumer.bootstrap_connected():
        raise Exception("Failed to connect to Kafka server")
    print("Connected to Kafka successfully.")
    if not consumer.topics():
        raise Exception("No topics found. Please ensure the topic exists.")
    print(f"Subscribed to topics: {consumer.topics()}")
    if not consumer.subscription():
        raise Exception("No subscription found. Please ensure the topic is subscribed.")
    print(f"Current subscription: {consumer.subscription()}")

    while True:
        for message in consumer:
            print(f"Received message: {message.value} from topic: {message.topic} at offset: {message.offset}")
            # Process the message as needed
        
except Exception as e:
    print(f"Error in Kafka consumer: {e}")
    exit(1)
finally:
    if 'consumer' in locals():
        consumer.close()
        print("Kafka Consumer closed successfully.")
    else:
        print("Consumer was not initialized.")

