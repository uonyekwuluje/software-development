#!/usr/bin/env python3
from kafka import KafkaConsumer
import pandas as pd

kafka_address = ["192.168.1.122:9092"]
kafka_topic = "exam"

consumer = KafkaConsumer(kafka_topic,
                         bootstrap_servers=kafka_address,
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000
                        )
consumer.subscribe([kafka_topic])

for message in consumer:
    #print("Received data: ", message)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    #print(f"Message: {message.value.decode('utf-8')}")
