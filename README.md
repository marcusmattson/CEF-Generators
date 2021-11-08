# CEF-Generators

Python scripts that can be modified to produce CEF log data. Output includes CEF-compliant headers and extensions, as well as additional custom keys.

1. **CEF Simulate**: Generate a CEF record and print to display
   * Modify `time.sleep()` for desired frequency
2. **CEF Simulate MQTT**: Generate a CEF record and publish to MQTT broker
   * modify `mqttc.connect("localhost", 1883)` for your MQTT broker
   * One-time execution that can be modified or embedded in another applicaiton for looping
3. **CEF Simulate Kafka**: Generate a CEF record and publish to Kafka topic
   * Modify `KafkaProducer(bootstrap_servers='192.168.142.111:9092')` for your Kafka bootstrap servers
   * Uncomment `#logging.basicConfig(level=logging.INFO)` to troubleshoot
   * One-time execution that can be modified or embedded in another applicaiton for looping

Content customization of the scripts is identical.

* Use/change the lists as needed
* `ts` is an event timestamp
* `ts_2` is an event timestamp designed to introduce occassional timestamp errors that are greater than the current time
* The varios random variables produce the sample data
