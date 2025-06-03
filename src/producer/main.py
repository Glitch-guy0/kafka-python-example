from kafka import KafkaProducer

try:
    producer = KafkaProducer(
        bootstrap_servers = ['localhost:9092'],
        value_serializer=lambda v: str(v).encode('utf-8'),
    )
    if not producer.bootstrap_connected():
        raise Exception("Failed to connect to Kafka server")
    
    producer.send('help1', "a new message from producer")
    producer.flush()
    print("Message sent successfully to 'help1' topic.")
    producer.close()

except Exception as e:
    print(f"Error in Kafka producer: {e}")
    exit(1)