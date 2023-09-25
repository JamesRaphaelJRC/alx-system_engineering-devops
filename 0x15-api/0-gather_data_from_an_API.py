#!/usr/bin/python3
'''Returns information about an employee TODO list progress'''
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(response)