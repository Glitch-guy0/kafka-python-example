# kafka-python-example

This repository demonstrates using [Apache Kafka](https://kafka.apache.org/) with Python via the [kafka-python](https://github.com/dpkp/kafka-python) client.

## Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/)
- Python 3.x

### Steps to Run the Project

1. **Start Kafka and Zookeeper using Docker Compose:**
    ```bash
    docker-compose up -d
    ```

2. **Initialize Kafka topics and partitions# kafka-python-example

This repository demonstrates using [Apache Kafka](https://kafka.apache.org/) with Python via the [kafka-python](https://github.com/dpkp/kafka-python) client.

## Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/)
- Python 3.x

### Steps to Run the Project

1. **Start Kafka using Docker Compose:**
    ```bash
    docker-compose up -d
    ```

2. **Initialize Kafka topics and partitions:**
    ```bash
    python src/admin/main.py
    ```

3. **Run Consumers:**
    - The consumer code is in `src/consumer/main.py`.
    - By default, a single consumer group instance is used.
    - You can run up to 3 consumer instances for parallel processing:
      ```bash
      python src/consumer/main.py
      # In separate terminals, run up to 2 more times for max 3 consumers
      ```

4. **Run Producer to send messages:**
    ```bash
    python src/producer/main.py
    ```
    - The producer sends string messages to the consumer.

---

Happy learning!
