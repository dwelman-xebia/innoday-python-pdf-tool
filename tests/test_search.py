from pdftool.search import search


def test_search():
    sentence = "The man walks. I am a nonsense other sentence?"

    result = search("man walks", sentence)

    assert result == ["The man walks."]


def test_insufficient_search_term_length():
    sentence = "something."

    result = search("s", sentence)

    assert result == ["Insufficient search-term length, minimum two characters!"]


def test_filter_for_all_Is():
    sentence = "I am a human. I am a developer! Have a nice day"

    result = search("I ", sentence)

    assert result == ["I am a human.", "I am a developer!"]

def test_casing_does_not_matter():
    sentence = "Capitalization does not matter. And capitalization does not matter again."

    result = search("cap", sentence)

    assert result == ["Capitalization does not matter.", "And capitalization does not matter again."]
