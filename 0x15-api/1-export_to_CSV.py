#!/usr/bin/python3
''' Returns information about an employee Todo list progress and stores
    the output in a csv file
'''
import csv
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': id}).json()
    name = employee.get('name')

    with open('{}.csv'.format(id), 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            writer.writerow([id, name, status, title])
