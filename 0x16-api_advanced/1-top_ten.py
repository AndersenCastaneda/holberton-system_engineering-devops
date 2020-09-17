#!/usr/bin/python3
"""
1-top_ten
"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json/'.format(subreddit)
    user_agent = {'User-Agent': 'Chrome/85.0.4183.102'}
    request = requests.get(url, headers=user_agent)
    if request.status_code == 200:
        subscribers = request.json().get('data').get('children')
        count = 0
        for hot in subscribers:
            if count == 10:
                break
            count += 1
            print(hot.get('data').get('title'))
    else:
        print(None)
