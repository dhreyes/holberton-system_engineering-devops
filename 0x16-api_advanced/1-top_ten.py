#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects
"""
import requests
import sys

def top_ten(subreddit):
    """
    Returns the titles of the first 10 hot posts listed for a given subreddit
    can handle special characters
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/78.0.3904.108'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()['data']['children']
        for i in range(10):
            print(data[i]['data']['title'])
    except:
        print(None)