from pypdf import PdfReader
import re


def read_content():
    reader = PdfReader("./commands/search/search.pdf")
    content = " ".join(page.extract_text().strip() for page in reader.pages)
    content = ' '.join(content.split())
    return split_sentences(content)


def search(search_term: str, content: str):
    return None


def split_sentences(st):
    st = st.strip() + '. '
    sentences = re.split(r'([.?!][.?!\s])+', st)
    return sentences[:-1]