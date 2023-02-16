from pypdf import PdfReader, PdfWriter
from argparse import ArgumentParser

from compress.compress import compress_page

import os

parser = ArgumentParser(description=__doc__)

def main():

    parser.add_argument("input_pdf_name", help="The name of the input PDF file")

    parser.add_argument(
        "-o", "--output",
        dest="output_pdf_name",
        help="The name for the PDF output file",
        required=False,
    )
    parser.add_argument(
        "-c", "--compress",
        dest="should_compress",
        action="store_true"
    )

    input_parameters, unknown_input_parameters = parser.parse_known_args()

    name = input_parameters.input_pdf_name
    output_name = output_name = name + "-output"

    if input_parameters.output_pdf_name is not None:
        output_name = input_parameters.output_pdf_name

    should_compress = False
    if input_parameters.should_compress is not None:
        should_compress = input_parameters.should_compress
        if should_compress is True:
            print("- Compression Enabled")
    
    if not name.endswith(".pdf"):
        print("File must end with '.pdf' extension")
        exit(-1)

    if not output_name.endswith(".pdf"):
        output_name += ".pdf"

    reader = PdfReader(name)
    
    input_file_stats = os.stat(name)
    print('''Input file stats:
        Size in bytes: {}
        Pages: {}
    '''.format(input_file_stats.st_size, len(reader.pages)))

    writer = PdfWriter()

    for page in reader.pages:
        if should_compress:
            page = compress_page(page)
        writer.add_page(page)

    with open("{}".format(output_name), "wb") as f:
        writer.write(f)

    output_file_stats = os.stat(output_name)
    reader = PdfReader(name)
    print('''Input file stats:
        Size in bytes: {}
        Pages: {}
    '''.format(output_file_stats.st_size, len(reader.pages)))

if __name__ == "__main__":
    main()