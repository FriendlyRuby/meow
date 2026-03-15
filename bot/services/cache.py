import time

CACHE = {}

CACHE_TTL = 3600  # 1 час


def get(key):

    if key not in CACHE:
        return None

    value, timestamp = CACHE[key]

    if time.time() - timestamp > CACHE_TTL:
        del CACHE[key]
        return None

    return value


def set(key, value):

    CACHE[key] = (value, time.time())