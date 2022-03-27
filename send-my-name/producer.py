import pika
import time, random

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()

messageID = 1

channel.queue_declare(queue='name-send')
while True:
    message = f"hello I am mgh27 messageID: {messageID}"
    channel.basic_publish(exchange='', routing_key='name-send', body=message)
    print(f"sent message:{message}")
    time.sleep(random.randint(1, 4))
    messageID += 1