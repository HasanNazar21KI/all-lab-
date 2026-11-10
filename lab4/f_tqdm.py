import time
from tqdm import tqdm


def progress(n):
    """tqdm: показує прогрес-бар."""
    for _ in tqdm(range(n), desc="Обробка"):
        time.sleep(0.02)
