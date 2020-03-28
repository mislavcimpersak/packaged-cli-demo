from os.path import join
from urllib.parse import urlparse

import requests


def download_file(url, name=None, destination=None):
    if name is None:
        path = urlparse(url).path
        if path:
            name = path.split("/")[-1]
        else:
            name = urlparse(url).netloc

    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()

    open(join(destination, name), "wb").write(response.content)
