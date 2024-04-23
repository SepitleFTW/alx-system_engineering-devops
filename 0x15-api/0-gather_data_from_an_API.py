#!/usr/bin/python3
"""
returns list for employee ID given
"""


import request
import sys


if __name__ == "__main__":
    # url for JSONplaceholder api
    url = 'https://jsonplaceholder.typicode.com/'

    # employees information by using employee ID
    employee_id = sys.rgv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # get to do list for the employee
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # filter the tasks and then count them up
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # print name and number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # print out tasks that are done with indent
    [print("\t {}".format(complete)) for complete in completed]
