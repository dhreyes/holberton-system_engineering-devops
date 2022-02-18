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
import requests
import sys
import json


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0'
            }
    if after is not None:
        url += '?after={}'.format(after)
    r = requests.get(url, headers=headers)
    if r.status_code == 404:
        return None
    if r.status_code == 200:
        data = r.json()
        hot_list += [x['data']['title'] for x in data['data']['children']]
        print(hot_list)
        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            return hot_list
    else:
        return None
