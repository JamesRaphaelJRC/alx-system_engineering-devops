#!/usr/bin/python3
''' Querries the Reddit API '''
import requests

"""
    def top_ten(subreddit):
        ''' Prints the titles of the first 10 hot posts listed for  given
            subreddit
        '''
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        headers = {"USer-Agent": "MyALXAdvancedAPiProjectBot (by /u/jamesrc)"}

        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts[:10]:
                print(post['data'].get('title'))
        else:
            print('None')
"""


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        [print(p.get("data").get("title")) for p in results.get("children")]
    else:
        print("None")
