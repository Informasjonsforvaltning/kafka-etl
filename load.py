import os

from dotenv import load_dotenv

load_dotenv()
SCHEMA_REG = os.environ.get("SCHEMA_REG")
SCHEMA_ID = os.environ.get("SCHEMA_ID")
KAFKA_SERVER = os.environ.get("KAFKA_SERVER")
TOPIC = os.environ.get("TOPIC")

with open('./messages_0.txt') as messages_file:

    load = f"""kubectl exec {SCHEMA_REG} -- bash -c "echo '{messages_file.read()}'|kafka-avro-console-producer --bootstrap-server {KAFKA_SERVER} --topic {TOPIC} --property value.schema.id={SCHEMA_ID}" """

    os.system(load)
