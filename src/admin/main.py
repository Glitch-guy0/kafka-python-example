from kafka.admin import NewTopic, KafkaAdminClient
from kafka.errors import TopicAlreadyExistsError


try:
    print("Connecting to Kafka as Admin...")
    kafka = KafkaAdminClient(
        bootstrap_servers="localhost:9092", client_id="admin_client"
    )
    print("Connected to Kafka successfully.")
except Exception as e:
    print(f"Failed connecting to kafka: {e}")
    exit(1)

print("Creating topics...")
help1 = NewTopic(name="help1", num_partitions=3, replication_factor=1)
help2 = NewTopic(name="help2", num_partitions=3, replication_factor=1)
try:
    kafka.create_topics(new_topics=[help1, help2], validate_only=False)
    print("Topics created successfully.")
except Exception as e:
    if isinstance(e, TopicAlreadyExistsError):
        print("Topics already exist, skipping creation.")
    else:
        print(f"Failed to create topics: {e}")
        exit(1)

kafka.close()
print("Kafka Admin closed successfully.")
