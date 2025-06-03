from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError, NoBrokersAvailable

try:
    print("Connecting to Kafka as Producer...")
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        # acks='all',
        # retries=3,
        # transactional_id='my_transactional_id',
        value_serializer=lambda x: x.encode('utf-8'),
        key_serializer=lambda x: x.encode('utf-8') if x else None,
        max_block_ms=10000,  # Set maximum block time for send operations
        request_timeout_ms=50000,  # Set request timeout for send operations
    )

    if producer.bootstrap_connected():
        print("Connected to Kafka successfully.")
        print(producer._metadata)

    # producer.init_transactions()
    def send_message(topic, key, message):
        try:
            # producer.begin_transaction()
            msg = producer.send(topic, key = key, value=message, partition=0)
            print(f"Message sent to {topic}: {msg}")
            msg.get(timeout=5)
            # producer.commit_transaction()
            print("commit successful")
        except Exception as e:
            # try:
            #     producer.abort_transaction()
            # except Exception as abort_e:
            #     print(f"Failed to abort transaction: {abort_e}")
            if isinstance(e, KafkaTimeoutError):
                print(f"Timeout error while sending message to {topic}")
            elif isinstance(e, TypeError):
                print(f"Invalid Topic: Topic must be a string, got {type(topic)}")
            elif isinstance(e, ValueError):
                print("Invalid Topic: Topic must be chars (a-zA-Z0-9._-), and less than 250 length")
            else:
                print(f"Failed to send message to {topic}: {e}")

    print("sending message to topic help1")
    send_message('help1', key='key1', message='Hello from help1 topic!')
    print("sending message to topic help2")
    send_message('help2', key='key2', message='Hello from help2 topic!')
    producer.flush()
    producer.close()
    print("Kafka Producer closed successfully.")
except Exception as e:
    if isinstance(e, NoBrokersAvailable):
        print("No Kafka brokers available. Please check your Kafka server.")
    else:
        print(f"Failed to create Kafka producer: {e}")
