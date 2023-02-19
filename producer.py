from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'data' : e}
    producer.send('foobar', value=data)
    print("sent data")
    sleep(2)
