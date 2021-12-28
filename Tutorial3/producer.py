import pika

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#ingreso de consulta en productor
message = input("Ingrese su busqueda de wikipedia: ")

#Creación de la colas
channel.queue_declare(queue='WikipediaResume')
channel.queue_declare(queue='WikipediaVisitas')

#publicacion de consulta para resumen en rabbitMQ
channel.basic_publish(exchange='',
                      routing_key='WikipediaResume',
                      body=message)

#publicacion de consulta para visitas en rabbitMQ
channel.basic_publish(exchange='',
                      routing_key='WikipediaVisitas',
                      body=message)

print(" [x] Sent " + message + " search to Wikipedia Consumers")

connection.close()