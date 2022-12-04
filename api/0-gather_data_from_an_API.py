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

    to_do_usr = [to for to in to_do_r if to.get("userId") == int(u_id)]
    complete_t = [com for com in to_do_usr if com.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(
                  u_request.get('name'),
                  len(complete_t),
                  len(to_do_usr)))

    for task in complete_t:
        print("\t " + task.get("title"))
