from app import get_random_text, TEXTS

def test_random_text_is_valid():
    text = get_random_text()
    assert text in TEXTS
