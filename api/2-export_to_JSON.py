#!/usr/bin/python3
""" module gather_data_from_an_API """

import requests
from sys import argv
import json


if __name__ == "__main__":
    "root of API: https://jsonplaceholder.typicode.com/"

    dict_result = {}
    u_id = argv[1]
    url_r = "https://jsonplaceholder.typicode.com/{}"

    u_request = requests.get(url_r.format("users/" + u_id)).json()
    to_do_r = requests.get(url_r.format("todos/")).json()

    dict_result[u_id] = []
    file_name = "{}.json".format(u_id)

    u_name = u_request.get("username")
    
    for task in to_do_r:
        dict_task = {}
        if task.get("userId") == int(u_id):
            dict_task["task"] = task.get("title")
            dict_task["completed"] = task.get("completed")
            dict_task["username"] = u_name
            dict_result[u_id].append(dict_task)

    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(dict_result, json_file)
