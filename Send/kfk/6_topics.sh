#!/bin/bash
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic aliens
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic encounters
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic locations
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic witnesses