#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"

    userID = int(argv[1])
    data = requests.get(url + f"users/{userID}").json()
    tasks = requests.get(f"{url}users/{userID}/todos").json()
    completed_tasks = []

    with open('{}.json'.format(userID), 'w+') as file:
        for all in tasks:
            all_data = {"task": all.get("title"),
                        "completed": all.get("completed"), "username": data}
            completed_tasks.append(all_data)
        info = {userID: completed_tasks}
        file.write(json.dumps(info))
