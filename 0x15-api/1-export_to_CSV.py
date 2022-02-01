#!/usr/bin/python3
"""Gather data from an API and export in CSV format"""
import requests
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        exit()

    employee_id = argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(site + 'users/' + employee_id).json()
    todos = requests.get(site + 'todos?userId=' + employee_id).json()
    name = user.get('name')
    done = [title['title'] for title in todos
            if title['completed'] is True]
    username = user.get('username')

    with open('{}.csv'.format(employee_id), 'w') as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(employee_id, username,
                                                   todo['completed'], todo['title']))
