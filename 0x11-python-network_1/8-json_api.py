#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a
parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

