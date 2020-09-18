#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a liste whit all hot articles
    titles for a given subreddit. If no results are found for the given
    subreddit, the function should return None."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Chrome/85.0.4183.102'}
    request = requests.get(url, headers=user_agent, params={'limit': 100,'after': after})

    if request.status_code == 200:
        posts = request.json().get('data').get('children')
        after = request.json().get('data').get('after')
    else:
        if hot_list == []:
            return None
        return hot_list

    if posts is None:
        if hot_list == []:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data').get('title'))

    if after is None:
        if hot_list == []:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
