from pypdf import PdfReader


def load_file():
    reader = PdfReader("./search.pdf")
    print(reader)