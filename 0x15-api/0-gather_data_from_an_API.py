#!/usr/bin/python3
# Returns information about his/her TODO list progress

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 2:
        uid = argv[1]
        u = 'https://jsonplaceholder.typicode.com/users/{}'.format(uid)
        t = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(uid)
        name = requests.get(u).json()['name']
        rq_todo = requests.get(t).json()
        tasks = [i['title'] for i in rq_todo if i['completed'] is True]
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(tasks), len(rq_todo)))
        print('\n'.join('\t{}'.format(i) for i in tasks))
