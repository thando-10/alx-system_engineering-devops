#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # URL for employee's todos
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # URL for employee's info
    user_url = f'{base_url}/users/{employee_id}'

    try:
        # Fetching data
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)

        # Checking if requests were successful
        if todos_response.status_code != 200 or user_response.status_code != 200:
            print("Failed to fetch data. Please try again later.")
            return

        # Parsing data
        todos_data = todos_response.json()
        user_data = user_response.json()

        # Extracting employee info
        employee_name = user_data['name']

        # Counting completed tasks
        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)
        completed_tasks_count = len(completed_tasks)

        # Displaying progress
        print(f"Employee {employee_name} is done with tasks ({completed_tasks_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data:", e)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

