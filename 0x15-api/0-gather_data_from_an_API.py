import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch user data
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        user_data = user_response.json()

        # Fetch todo list
        todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
        todos_data = todos_response.json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todos_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos_data)

        # Display information
        print(f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task_title in completed_tasks:
            print(f"\t{task_title}")

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
