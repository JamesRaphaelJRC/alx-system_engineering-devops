#!/usr/bin/python3
''' Queries the Reddit API'''
import requests


def number_of_subscribers(subreddit):
    ''' Returns the number of suscribers in a valid subreddit
        Returns 0 if the subreddit is invalid
    '''
    # Setting Reddit API endpoint URL for subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Setting a custom User-Agent to avoid too many requests error
    headers = {"USer-Agent": "MyALXAdvancedAPiProjectBot (by /u/jamesrc)"}

    # Sending a GET request to the Reddit API endpoint disallowing redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subreddit_data = response.json().get('data')
        subscribers_count = subreddit_data.get('subscribers')
        return subscribers_count
    else:
        return 0
