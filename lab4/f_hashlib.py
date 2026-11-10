import hashlib


def sha256_of(text):
    """hashlib (вбудована): SHA-256 хеш рядка."""
    return hashlib.sha256(text.encode()).hexdigest()
