### 在docker中进行Kafka安装

安装相关插件

~~~bash
wget https://archive.apache.org/dist/kafka/3.7.1/kafka_2.12-3.7.1.tgz
tar -xzf kafka_2.12-3.7.1.tgz
mv kafka_2.12-3.7.1 kafka #重命名
mv kafka /usr/local
#安装java和python下的kafka
apt-get update
apt-get install -y openjdk-11-jre
pip install kafka-python
~~~

运行kafka服务器并进行测试

~~~bash
#第一个终端,启动 ZooKeeper
/usr/local/kafka/bin/zookeeper-server-start.sh /usr/local/kafka/config/zookeeper.properties
#第二个终端,启动 Kafka 服务器
/usr/local/kafka/bin/kafka-server-start.sh /usr/local/kafka/config/server.properties
#第三个终端,运行测试脚本
python kafka_test.py
~~~





