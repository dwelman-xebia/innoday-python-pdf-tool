from pypdf import PdfReader


def load_file():
    reader = PdfReader("./search/search.pdf")
    print(reader)
