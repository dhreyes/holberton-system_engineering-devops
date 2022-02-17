#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API, parses the title
of all the hot articles, and prints a sorted count of given keywords
(case-insensitvie, delimited by spaces. Javascript should count as javascript, but java should not)
Requirements:
- Prototype: def count_words(subreddit, word_list)
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied
and a list of keywords.
- If word_list contains the same word (case insensitive), the final count should be the sum
of each duplicate (example below with java)
- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in. java java java counts as 3 separate occurrences of java.
- To make life easier, java. or java! or java_ should not count as java
- If no posts match or the subreddit is invalid, print nothing.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.
"""
import requests
import sys


def count_words(subreddit, word_list):
    """
    Counts the number of times a word appears in a subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print(None)
        return
    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['title'] for post in data['data']['children']]
        for word in word_list:
            count = titles.count(word)
            print('{}: {}'.format(word, count))
    else:
        print(None)