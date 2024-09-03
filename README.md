# Kafka Docker Compose Example

This repository demonstrates how to set up Apache Kafka with Docker Compose and includes Python scripts for producing and consuming messages.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.x
- Poetry (for dependency management)

## Setup

### Start Kafka and Zookeeper

Ensure you have a `docker-compose.yml` file in the root directory of the repository. To start Kafka and Zookeeper, run:

```bash
docker-compose up -d
```
### Install Dependencies
Install the required Python dependencies using Poetry:

```bash
poetry install
```

### Produce Messages
Run the Kafka producer script to send messages to a Kafka topic:
```bash
poetry run python3 producer.py
```

### Consume Messages
Run the Kafka consumer script to receive messages from a Kafka topic:

```bash
poetry run python3 consumer.py
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.