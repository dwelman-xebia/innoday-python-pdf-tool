from typing import List
import re


def search(search_term: str, content: str) -> List[str]:
    if len(search_term) < 2:
        return ["Insufficient search-term length, minimum two characters!"]
    split_content = split_sentences(content)
    return [sentence for sentence in split_content if search_term.lower() in sentence.lower()]


def split_sentences(st):
    st = st.strip() + '. '
    pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
    sentences = pat.findall(st)
    return sentences
