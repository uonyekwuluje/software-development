#!/usr/bin/env python3

import click
from confluent_kafka.admin import AdminClient, NewTopic

kafka_address = "192.168.1.122:9092"
admin_client = AdminClient(
    {'bootstrap.servers': kafka_address}
 )

@click.group(invoke_without_command=True, chain=True)
def cli():
    pass


@cli.command()
@click.option('-t', '--new_topic', help="New Kafka Topic")
def create_topic(new_topic):
    topic_list = []
    topic_list.append(NewTopic(new_topic, num_partitions=1, replication_factor=1))
    fs = admin_client.create_topics(topic_list)

    for topic, f in fs.items():
        try:
            f.result()  
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))


@cli.command()
@click.option('-t', '--topic_name', help="Kafka Topic to Delete")
def delete_topic(topic_name):
    try:
        admin_client.delete_topics([topic_name])
        print(f"{topic_name} Topic Deleted")
    except Exception as e:
        print(f"[{topic_name}] Topic Doesn't Exist")
        print("The Error is:=> ",e)



if __name__ == '__main__':
    cli()
