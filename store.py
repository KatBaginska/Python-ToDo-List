import json
import os

file = 'task_storage.json'
def load_task():
    with open('task_storage.json', 'r') as file:
        return json.load(file)
def save_task(tasks):
    with open('task_storage.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    