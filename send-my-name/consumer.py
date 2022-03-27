import pika
import time
import random
def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"[x] received {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("finish processing message")

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()

channel.queue_declare(queue='name-send')

# each consumer process one message at the time
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='name-send', on_message_callback=on_message_received)

print("[*] Start listening for message.")

channel.start_consuming()