from typing import List

from pdftool.search import search
from pypdf import PdfReader


def read_content(pdf_filepath: str) -> List[str]:
    reader = PdfReader(pdf_filepath)
    content = " ".join(page.extract_text().strip() for page in reader.pages)
    content = ' '.join(content.split())
    return content


def test_search():
    sentence = "The man walks. I am a nonsesne other sentence?"

    result = search("man walks", sentence)

    assert result == ["The man walks."]


def test_insufficient_search_term_length():
    sentence = "something."

    result = search("s", sentence)

    assert result == "Insufficient search-term length, minimum two characters!"


def test_filter_for_all_Is():
    sentence = "I am a human. I am a developer! Have a nice day"

    result = search("I ", sentence)

    assert result == ["I am a human.", "I am a developer!"]
