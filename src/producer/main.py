from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError, NoBrokersAvailable

try:
    print("Connecting to Kafka as Producer...")
    producer = KafkaProducer(
        bootstrap_servers='192.168.29.55:9092',
        acks='all',
        retries=3,
        transactional_id='my_transactional_id',
    )
    print("Connected to Kafka successfully.")

    def send_message(topic, message):
        try:
            producer.init_transactions()
            producer.begin_transaction()
            msg = producer.send(topic, value=message.encode('utf-8'))
            msg.get(timeout=10)  # Wait for the message to be sent
            print(f"Message sent to {topic}: {msg}")
            producer.commit_transaction()
        except Exception as e:
            try:
                producer.abort_transaction()
            except Exception as abort_e:
                print(f"Failed to abort transaction: {abort_e}")
            if isinstance(e, KafkaTimeoutError):
                print(f"Timeout error while sending message to {topic}")
            elif isinstance(e, TypeError):
                print(f"Invalid Topic: Topic must be a string, got {type(topic)}")
            elif isinstance(e, ValueError):
                print("Invalid Topic: Topic must be chars (a-zA-Z0-9._-), and less than 250 length")
            else:
                print(f"Failed to send message to {topic}: {e}")

    print("sending message to topic help1")
    send_message('help1', 'Hello from help1 topic!')
    print("sending message to topic help2")
    send_message('help2', 'Hello from help2 topic!')

    producer.close()
    print("Kafka Producer closed successfully.")
except Exception as e:
    if isinstance(e, NoBrokersAvailable):
        print("No Kafka brokers available. Please check your Kafka server.")
    else:
        print(f"Failed to create Kafka producer: {e}")
