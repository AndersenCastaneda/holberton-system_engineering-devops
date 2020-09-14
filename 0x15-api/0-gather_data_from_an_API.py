#!/usr/bin/python3
# Returns information about his/her TODO list progress

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        uid = sys.argv[1]
        u = 'https://jsonplaceholder.typicode.com/users/{}'.format(uid)
        t = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(uid)
        name = requests.get(u).json().get('name')
        rq_todo = requests.get(t).json()
        tasks = [i.get('title') for i in rq_todo if i.get('completed') is True]
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(tasks), len(rq_todo)))
        print('\n'.join('\t {}'.format(i) for i in tasks))
