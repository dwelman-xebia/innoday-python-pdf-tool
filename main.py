from PyPDF2 import PdfReader, PdfWriter
import sys

def main():
    name = "mypdf.pdf"

    reader = PdfReader(name)
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open("{}-decrypted.pdf".format(name), "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    main()