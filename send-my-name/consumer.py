import pika

def on_message_received(ch, method, properties, body):
    print(f"[x] received {body}")

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()

channel.queue_declare(queue='name-send')

channel.basic_consume(queue='name-send', auto_ack=True, on_message_callback=on_message_received)

print("[*] Start listening for message.")

channel.start_consuming()