#!/usr/bin/python3
""" Python script that, for a given employeee ID, returns information bout his/her TODO list progress"""
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
    done = [title['title'] for title in todos if title['completed'] is True]
    print("Employee {} is done with tasks({}/{}):".format(name, len(done), len(todos)))

    for task in done:
        print("\t {}".format(task))