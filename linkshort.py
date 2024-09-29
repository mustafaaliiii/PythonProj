# -*- coding: utf-8 -*-
"""
@author: musta
"""

import requests

def shorten_url(long_url):
    api_url = "http://tinyurl.com/api-create.php"
    params = {'url': long_url}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.text  # The short URL
    else:
        return f"Error: Unable to shorten the URL. Status code: {response.status_code}"

def main():
    print("Welcome to the URL Shortener by Mustafa!")
    long_url = input("Enter the long URL to shorten: ")

    short_url = shorten_url(long_url)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
