#!/usr/bin/python3
"""Script that fetch number of subscriber for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers is @subreddit is valid subreddit.
    if not return 0."""

    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://reddit.com/r/{}.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        subscriber_number = json_data.get('data').get(
            'children')[0].get('data').get('subreddit_subscribers')
        return subscriber_number
    else:
        return 0

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

