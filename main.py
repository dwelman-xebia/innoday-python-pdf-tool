from PyPDF2 import PdfReader, PdfWriter
from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)

def main():

    parser.add_argument(
        "-n",
        dest="pdf_name",
        help="PDF Name",
        required=True,
    )

    input_parameters, unknown_input_parameters = parser.parse_known_args()

    name = input_parameters.pdf_name

    print("-n: {}".format(name))

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