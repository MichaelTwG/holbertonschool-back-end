#!/usr/bin/python3
""" module gather_data_from_an_API """

import json
import requests
from sys import argv


if __name__ == "__main__":
    "root of API: https://jsonplaceholder.typicode.com/"

    dict_result = {}
    url_r = "https://jsonplaceholder.typicode.com/{}"

    u_request = requests.get(url_r.format("users/")).json()
    to_do_r = requests.get(url_r.format("todos/")).json()

    file_name = "todo_all_employees.json"

    for user in u_request:
        u_id = user.get("id")
        dict_result[u_id] = []
        u_name = user.get("username")
        for task in to_do_r:
            dict_task = {}
            if task.get("userId") == int(u_id):
                dict_task["task"] = task.get("title")
                dict_task["completed"] = task.get("completed")
                dict_task["username"] = u_name
                dict_result[u_id].append(dict_task)

    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(dict_result, json_file)
