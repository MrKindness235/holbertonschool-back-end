#!/usr/bin/python3
"""Script that using this REST API, for a given employee ID."""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    userID = int(argv[1])
    data = requests.get(url + f"users/{userID}").json()
    tasks = requests.get(f"{url}users/{userID}/todos").json()
    completed_tasks = []
    for task in tasks:
        if task["completed"]:
            completed_tasks.append(task)

    print(f"Employee {data['name']} is done with ", end="")
    print(f"tasks({len(completed_tasks)}/{len(tasks)}):")

    for tasks in completed_tasks:
        print(f"\t + {tasks['title']}")
