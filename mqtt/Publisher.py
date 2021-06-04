# Publisher.py
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTTServerIP = "localhost"
MQTTServerPort = 1883 #port
MQTTTopicName = "MYTOPIC" #TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(MQTTServerIP, MQTTServerPort)
mqttc.publish(MQTTTopicName, "1")
publish.single(MQTTTopicName,"2")
