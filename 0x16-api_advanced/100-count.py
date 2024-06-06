#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""

import requests

def count_words(subreddit, word_list, word_list, after=None, count=[]):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords

    "https://www.reddit.com/r/{}/hot.json"
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/10.0/API'}

    params = {'limit': 100}

    if after:
        
        params['after'] = after

        reponse = requests.get(url,
                headers=headers,
                params=params, allow_redirects=False)

        if reponse.status_code != 200:
            return

        main_data = reponse.json()

        data = main_data.get('data')

        children = data.get('children')

        for post in children:
            title = post.get('data', {}).get('title').lower()

            for word in word_list:
                if word.lower() in title:

                    counts[word] = counts.get(word, 0) + title.count(word.lower())


                    after = main_data.get('data', {}).get('after')

                    if after:

                        count_words(subreddt, word_list, after, counts)
                    else:
                        sorted_counts = sorted(counts.items(),
                                key=lambda x: (-x[1], x[0].lower()))

                        for word, count in sorted_counts:
                                print(f"(word.lower()): {count}")



                       if __name__ == '__main__':
                           if len(sys.argv) < 3:
                                print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
                                print("Ex: {} programming 'python java javascript'". format(sys.argv[0]))
                                else:
                                result = count_words(sys.argv[1], [x for x in sys.agrv[2].split()])
