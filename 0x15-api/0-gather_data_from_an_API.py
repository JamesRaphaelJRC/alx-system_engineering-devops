#!/usr/bin/python3
'''Returns information about an employee Todo list progress'''
import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(id)).json()
    name = employee.get('name')
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.get('completed') is True)

    print("Employee {} is done with tasks({}/{})".format(name, completed_tasks,
                                                         total_tasks))
    for task in tasks:
        if task.get('completed'):
            print("\t{}".format(task.get('title')))