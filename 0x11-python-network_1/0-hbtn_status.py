#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib."""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    the_page = response.read()

print("Body response:")
print("\t- type:", type(the_page))
print("\t- content:", the_page)
print("\t- utf8 content:", the_page.decode("utf-8"))

