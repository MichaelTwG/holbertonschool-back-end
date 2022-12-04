#!/usr/bin/python3
""" module gather_data_from_an_API """

import requests
from sys import argv


if __name__ == "__main__":
    "root of API: https://jsonplaceholder.typicode.com/"

    u_id = argv[1]
    url_r = "https://jsonplaceholder.typicode.com/{}"

    u_request = requests.get(url_r.format("users/" + u_id)).json()
    to_do_r = requests.get(url_r.format("todos/")).json()

    u_name = u_request.get("username")
    file_name = "{}.csv".format(u_id)
    csv = ""
    for task in to_do_r:
        if task.get("userId") == int(u_id):
            task_status = task.get("completed")
            task_title = task.get("title")

            text = '"{}","{}","{}","{}"'.format(u_id,
                                                u_name,
                                                task_status,
                                                task_title)
            csv += text + "\n"
    with open(file_name, "w", encoding="utf-8") as csv_file:
        csv_file.write(csv)
