#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given
subreddit, the function should return None
Hint: The Reddit API uses pagination for separating
pages of responses
Requirements:
- Prototype: def recurse(subreddit, hot_list=[]):
- Note: You may change the prototype, but it must be able to be
called with just a subreddit supplied.
AKA you can add a counter, but it must work without supplying
a starting value in the main
- If not a valid subreddit, return None
- NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""
from tkinter import W
import requests
import sys
import json


def recurse(subreddit, hot_list=[], after=None):
    """Shows hot post"""
    hot_post = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    agent = {'User-Agent': 'requested'}
    parameters = {'after': after, 'limit': '100'}
    response = requests.get(url, headers=agent,
                            params=parameters, allow_redirects=False)
    if response.status_code in [302, 404]:
        return None
    if r.status_code == 200:
        data = r.json()
        hot_list += [x['data']['title'] for x in data['data']['children']]
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list
    else:
        posts = response.json()['data']['children']
        after = response.json()['data']['after']
        for hot in posts:
            hot_list.append(hot)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list