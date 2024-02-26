#!/usr/bin/python3
"""
0-main
"""
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for the given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        try:
            json_data = response.json()
            subscriber_count = json_data['data']['subscribers']
            return subscriber_count
        except KeyError:
            return 0
    else:
        return 0
