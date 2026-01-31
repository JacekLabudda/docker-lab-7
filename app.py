import random

TEXTS = [
    "Hello world",
    "Python jest super",
    "Docker jest fajny",
    "GitHub Actions działa"
]

def get_random_text():
    return random.choice(TEXTS)

if __name__ == "__main__":
    print(get_random_text())
