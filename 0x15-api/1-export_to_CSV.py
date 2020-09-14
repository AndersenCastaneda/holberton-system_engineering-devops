#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    if len(sys.argv) == 2:
        uid = sys.argv[1]
        u = 'https://jsonplaceholder.typicode.com/users/{}'.format(uid)
        t = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(uid)
        name = requests.get(u).json().get('username')
        rq_todo = requests.get(t).json()
        with open('{}.csv'.format(uid), 'w+') as file:
            for line in rq_todo:
                info = '"{}","{}","{}","{}"\n'.format(uid, name, line.get('completed'), line.get('title'))
                file.write(info)
