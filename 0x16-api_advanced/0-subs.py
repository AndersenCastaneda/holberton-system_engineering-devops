#!/usr/bin/python3
"""
0-subs
"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    import requests

    if subreddit is None or type(subreddit) != str:
        return 0

    url = 'https://www.reddit.com/r/programming/about.json'
    user_agent = {'User-agent': 'Chrome/85.0.4183.102'}
    request = requests.get(url, headers=user_agent)
    subscribers = request.json().get('data').get('subscribers')
    return (subscribers)

if __name__ == "__main__":
    pass
