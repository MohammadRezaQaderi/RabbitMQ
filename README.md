# RabbitMQ
RabbitMQ is an open-source message broker that implements AMQP (Advanced Message Queue Protocol).

## setup 

We can pull the RabbitMQ image first and run a container then or we run this command to do both
```text
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```
About this docker commands:
- **-it**: Run a container in interactive mode.This means you can execute commands inside the container while it is still running.
- **--rm**: Automatically remove the container when it exits.
- **--name**: Name of the container.
- **-p**: Publish a container's port(s) to the host.

Now we can then open the RabbitMQ on our browser located on [http://localhost:15672/](http://localhost:15672/). The default
username and password is `guest`.

## Using Python (send-my-name)
### Install library
```text
pip install pika
```
### Producer
We have Producer to send the message by channel to Consumer, we need channel first.
After import pika, we need to create a connection and a channel.
```python
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel  = connection.channel()
```

We need queue to control the message send by Producer, We can create a queue using the following line by give name to it.
```python
channel.queue_declare(queue='name-send')
```

The best and easiest way to publish a message on the queue is by using `.basic_public` method.
```python
message = "hello I am mgh27"
channel.basic_publish(exchange='', routing_key='name-send', body=message)
```
Finally, we close the connection in Producer side.
```python
connection.close()
```