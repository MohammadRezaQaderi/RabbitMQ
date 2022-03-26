import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()

channel.queue_declare(queue='letterbox')

message = "hello I am mgh27"