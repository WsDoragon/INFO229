import pika, sys, os, wikipedia, pageviewapi.period

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola
    channel.queue_declare(queue='WikipediaVisitas')

    def callback(ch, method, properties, body):
        count = pageviewapi.period.sum_last("en.wikipedia", body.decode(), last=365) #observamos la cantidad de visitas que tuvo la busqueda
        #Seteado en wikipedia ingles debido a problemas al probar la API
        
        #count = 10 # limpieza de cola

        #Imprimimos la cantidad de visitas
        print(" [x] Received %r" % body +". las consultas para este termino en los ultimos dias son: " + str(count))

    # Se consume la consulta en rabbitMQ
    channel.basic_consume(queue='WikipediaVisitas', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


        #Bocle infinita
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)