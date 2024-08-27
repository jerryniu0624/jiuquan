import json
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

# 读取配置文件
def read_config():
    with open('config_kafka.json', 'r') as f:
        config = json.load(f)
    return config

# 创建生产者
def create_producer(bootstrap_servers):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

# 发送消息
def send_message(producer, topic, message):
    try:
        future = producer.send(topic, message)
        result = future.get(timeout=10)
        print(f'Message sent: {result}')
    except KafkaError as e:
        print(f'Failed to send message: {e}')

# 创建消费者
def create_consumer(bootstrap_servers):
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='test-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    return consumer

# 接收消息
def consume_messages(consumer):
    for message in consumer:
        print(f'Consumed message: {message.value}')

if __name__ == '__main__':
    config = read_config()
    bootstrap_servers = config['kafka']['bootstrap_servers']

    producer = create_producer(bootstrap_servers)
    topic = 'test_topic'
    message = {'key': 'value'}
    send_message(producer, topic, message)

    consumer = create_consumer(bootstrap_servers)
    consume_messages(consumer)
