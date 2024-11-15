#!/usr/bin/env python3

import click
from kafka.admin import KafkaAdminClient, NewTopic

kafka_address = "192.168.1.121:9092"
admin_client = KafkaAdminClient(bootstrap_servers=kafka_address)

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.pass_context
@click.option('-t', '--new_topic', help="New Kafka Topic")
def create_topic(new_topic, ctx):
    topic_list = []
    topic_list.append(NewTopic(name=new_topic, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

@cli.command()
@click.pass_context
@click.option('-t', '--topic_name', help="Kafka Topic Name")
def delete_topic(topic_name, ctx):
    try:
        admin_client.delete_topics([topic_name])
        print(f"{topic_name} Topic Deleted")
    except Exception as e:
        print(f"[{topic_name}] Topic Doesn't Exist")
        print("The Error is:=> ",e)


if __name__ == '__main__':
    cli()
