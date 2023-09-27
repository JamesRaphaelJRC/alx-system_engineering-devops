#!/usr/bin/python3
''' Returns information about an employee Todo list progress and stores
    the output in a json file
'''
import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': id}).json()
    user_name = employee.get('username')

    with open('{}.json'.format(id), 'w', newline="") as jsonfile:
        json.dump({id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        } for task in tasks]}, jsonfile)
