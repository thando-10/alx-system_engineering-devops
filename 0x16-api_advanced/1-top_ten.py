#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)

# Example usage:
subreddit = "python"
print(f"Top 10 hot posts in r/{subreddit}:")
top_ten(subreddit)

