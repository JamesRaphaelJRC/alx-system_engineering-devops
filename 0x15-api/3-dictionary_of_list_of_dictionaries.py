#!/usr/bin/python3
''' Returns information about an employee Todo list progress and stores
    the output in a json file
'''
import json
import requests


if __name__ == '__main__':
    employees = requests.get('https://jsonplaceholder.typicode.com/users/'
                             ).json()
    all_employee_data = {}

    with open("todo_all_employees.json", "w") as todo_all:
        for employee in employees:
            id = employee.get('id')
            username = employee.get('username')
            tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                                 params='userId={}'.format(id)).json()
            task_info = [{"username": username, "task": task.get('title'),
                         "completed": task.get('completed')} for task in tasks]
            all_employee_data[id] = task_info

        json.dump(all_employee_data, todo_all)
