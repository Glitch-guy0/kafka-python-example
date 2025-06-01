# kafka-python

Welcome to my learning journey with **kafka-python**! This repository documents my exploration of using [Apache Kafka](https://kafka.apache.org/) with Python.

## Overview

## TODO List

- [ ] Create a consumer that subscribes to two different topics
- [ ] Implement a producer script
- [ ] Build a gateway for load balancing between consumers
- [ ] Enhance the producer to send custom messages
- [ ] Set up performance testing for producer and consumer

## Making Consumers Scalable

Kafka's design allows you to scale consumers horizontally. By running multiple consumer instances (either as separate containers or processes), you can distribute the workload of processing messages from a topic. Each consumer in the same consumer group will automatically receive a subset of the messages, enabling parallel processing and improved throughput. To scale, simply start more consumer containers or processes—Kafka will handle partition assignment and load balancing.

## What is kafka-python?

[kafka-python](https://github.com/dpkp/kafka-python) is a Python client for Apache Kafka, a distributed streaming platform. It allows Python applications to publish and consume messages from Kafka topics.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/)
- Python 3.x

## Usage

### Running the Consumer with Docker Compose

This command starts the full stack, which runs Nginx (as a gateway), the consumer services, and Kafka itself.

```bash
docker-compose up -d
```

### Producer

Run the producer script to send messages to a topic:

```bash
python producer.py
```

## Key Concepts

- **Producer**: Sends messages to Kafka topics.
- **Consumer**: Reads messages from Kafka topics.
- **Topic**: A named stream of records.

## Resources

- [Kafka Concepts](https://kafka.apache.org/documentation/#intro_concepts)

## My Learning Notes

- Docker Compose makes it easy to set up Kafka locally.
- Multiple consumers can read from the same topic, demonstrating Kafka's scalability.
- kafka-python provides a simple API for both producing and consuming messages.

---

Happy learning!

