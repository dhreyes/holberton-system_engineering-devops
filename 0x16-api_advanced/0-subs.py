#!/usr/bin/python3
"""
Write a function that queires the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Requirements:
- Prototype: def number_of_subscribers(subreddit)
- If not a valid subreddit, return 0
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    site = 'https://www.reddit.com/r/'
    url = site + subreddit + '/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0