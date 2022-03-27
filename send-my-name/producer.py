import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()

channel.queue_declare(queue='name-send')

message = "hello I am mgh27"
channel.basic_publish(exchange='', routing_key='name-send', body=message)

print(f"sent message:{message}")

connection.close()