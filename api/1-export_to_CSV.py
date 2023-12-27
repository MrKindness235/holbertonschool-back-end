#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format."""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"

    userID = int(argv[1])
    data = requests.get(url + f"users/{userID}").json()
    tasks = requests.get(f"{url}users/{userID}/todos").json()
    completed_tasks = []

    with open('{}.csv'.format(userID), 'w+') as file:
        for all in tasks:
            all_data = '"{}","{}","{}","{}"\n'.format(
                userID, data, all.get('completed'), all.get('title'))
            file.write(all_data)
