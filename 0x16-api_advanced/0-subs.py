#!/usr/bin/python3
"""
0-subs
"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Chrome/85.0.4183.102'}
    request = requests.get(url, headers=user_agent)
    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers

    return 0
