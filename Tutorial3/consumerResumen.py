import pika, sys, os, wikipedia
from wikipedia.wikipedia import suggest

def main():

    #Conexión al servidor RabbitMQ   
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #Nos aseguramos que existe una cola
    channel.queue_declare(queue='WikipediaResume')


    def callback(ch, method, properties, body):
        wikipedia.set_lang("es") #seteamos idioma de busqueda
        resume = wikipedia.summary(body,auto_suggest=True) #realizamos busqueda y entregamos resumen

        print(" [x] Received "+ body.decode() +" and the resume is: %r"  %resume +"\n\n")
        print(' [*] Waiting for messages. To exit press CTRL+C')

    #Consumimos la consulta en rabbitMQ
    channel.basic_consume(queue='WikipediaResume', on_message_callback=callback, auto_ack=True)
    

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