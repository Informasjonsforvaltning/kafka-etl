# kafka-etl

python scripts to generate kafka messages missing from the topics of a kafka-instance running in a cluster connected to the local kubectl

## Setup

```
% pip install -r requirements.txt
```

.env:

```
MESSAGE_TYPE=RESOURCE_REMOVED
SCHEMA_REG=schema-registry
SCHEMA_ID=1
KAFKA_SERVER=kafka:port
TOPIC=kafka-topic
```

MESSAGE_TYPE is the kafka message type
SCHEMA_REG is the podname for the schema-registry
SCHEMA_ID is the registered id for the schema
KAFKA_SERVER is the advertised listener in kafka
TOPIC is the kafka topic

## Generate missing remove messages
add meta data from the harvester to `harvester_export.json` and the list of non removed resources in kafka messages to `kafka_export.json`
```
% python generate_rm_messages.py
```

## Load

```
% python load.py
```
