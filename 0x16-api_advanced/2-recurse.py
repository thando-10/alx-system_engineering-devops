#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively query the Reddit API and return a list containing the titles of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): A list containing the titles of hot articles (default is an empty list).

    Returns:
    list: A list containing the titles of all hot articles for the given subreddit. Returns None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}  # Number of posts per request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if data['data']['children']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            # Recursive call to fetch more posts if available
            last_post = data['data']['children'][-1]['data']['name']
            params['after'] = last_post
            recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None

# Example usage:
subreddit = "python"
hot_articles = recurse(subreddit)
if hot_articles:
    print(f"All hot articles in r/{subreddit}:")
    for title in hot_articles:
        print(title)
else:
    print(None)

