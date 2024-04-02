import json
import os
import time

from dotenv import load_dotenv

load_dotenv()


def millis_now():
    return int(round(time.time() * 1000))


def create_rm_message(fdk_id):
    return "{" + f""" \\"type\\": \\"{os.environ.get("MESSAGE_TYPE")}\\", \\"fdkId\\": \\"{fdk_id}\\", \\"timestamp\\": {millis_now()}, \\"graph\\": \\"\\" """ + "}"


message_list = list()
with open('./kafka_export.json') as kafka_export_file:
    kafka_objects = json.load(kafka_export_file)
    kafka_ids = list()
    for obj in kafka_objects:
        kafka_ids.append(obj["id"])

    with open('./harvester_export.json') as harvester_export_file:
        harvester_meta = json.load(harvester_export_file)
        harvester_ids = list()
        for obj in harvester_meta:
            if obj.get("removed") is not True:
                harvester_ids.append(obj["fdkId"])

        for kafka_id in kafka_ids:
            if kafka_id not in harvester_ids:
                message_list.append(create_rm_message(kafka_id))

file_count = 0
while file_count + 500 < len(message_list):
    messages = "\n".join(message_list[file_count:file_count + 499])
    with open(f"messages_{file_count}.txt", 'w', encoding="utf-8") as messages_file:
        messages_file.write(messages)
    file_count = file_count + 500
