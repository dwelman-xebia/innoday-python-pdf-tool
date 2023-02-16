from typing import List

from pypdf import PdfReader
import re


def search(search_term: str, content: str) -> List[str] | str:
    if len(search_term) < 2:
        return "Insufficient search-term length, minimum two characters!"
    splitted_content = split_sentences(content)
    return [sentence for sentence in splitted_content if search_term in sentence]


def split_sentences(st):
    st = st.strip() + '. '
    pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    sentences = pat.findall(st)
    return sentences