import sys

import requests


def get_size(url):
    response = requests.get(url, allow_redirects=True, stream=True)
    response.raise_for_status()

    sys.stdout.write(response.headers.get("Content-Length", "unable to determine size"))
