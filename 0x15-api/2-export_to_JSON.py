#!/usr/bin/python3
"""Gather data from an API and exports
data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        exit()
    
    employee_id = sys.argv[1]
    site = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(site + 'users/' + employee_id).json()
    todos = requests.get(site + 'todos?userId=' + employee_id).json()
    name = user.get('name')
    done = [title['title'] for title in todos
            if title['completed'] is True]
    username = user.get('username')
    outToDo = []
    for todo in todos:
        outToDo.append({'task': todo['title'],
                        'completed': todo['completed'],
                        'username': username})
    out = {employee_id: {'name': name, 'todos': outToDo}}
    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(out, f)