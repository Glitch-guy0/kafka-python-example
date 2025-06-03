from kafka import KafkaProducer

try:
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: str(v).encode("utf-8"),
    )
    if not producer.bootstrap_connected():
        raise Exception("Failed to connect to Kafka server")

    while True:
        message = input("Enter message to send to 'help1' topic (or 'exit' to quit): ")
        if message.lower() == "exit":
            print("Exiting producer...")
            break
        if not message:
            print("Message cannot be empty. Please enter a valid message.")
            continue
        partition_input = input("Enter partition number (or leave empty for default): ")
        partition = int(partition_input) if partition_input.strip() else None
        producer.send("help1", message, partition=partition)
        producer.flush()

    producer.close()

except Exception as e:
    print(f"Error in Kafka producer: {e}")
    exit(1)
