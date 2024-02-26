import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for the given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', None)
        if data:
            return data.get('subscribers', 0)
    return 0
