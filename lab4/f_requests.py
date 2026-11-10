import requests


def build_url(base, params):
    """requests: формує URL із параметрами без відправки запиту."""
    return requests.Request("GET", base, params=params).prepare().url
