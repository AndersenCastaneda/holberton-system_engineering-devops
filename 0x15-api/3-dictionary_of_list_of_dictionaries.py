#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""

if __name__ == "__main__":
    import json
    import requests

    u = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(u).json()
    info = {}
    for user in users:
        uid = user.get('id')
        name = user.get('username')
        t = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(uid)
        rq_todo = requests.get(t).json()
        tasks = []
        for td in rq_todo:
            task = {"username": name, "task": td.get("title"),
                    "completed": td.get("completed")}
            tasks.append(task)
        info[uid] = tasks
    with open('todo_all_employees.json', 'w+') as file:
        file.write(json.dumps(info))
