#!/usr/bin/env python3

from kafka import KafkaProducer

kafka_address = ["192.168.1.122:9092"]
producer = KafkaProducer(
    bootstrap_servers =  kafka_address
 )
kafka_topic = "exam"

#producer.send(kafka_topic, b'Send Message One')
#producer.flush()

#producer.send(kafka_topic, b'Send Message Two')
#producer.flush()

#producer.send(kafka_topic, b'Send Message Three')
#producer.flush()

producer.send(kafka_topic, b'Latest Message Sent. Go Figure')
producer.flush()
