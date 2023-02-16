from pypdf import PdfReader, PdfWriter
from argparse import ArgumentParser

parser = ArgumentParser(description=__doc__)

def main():

    parser.add_argument("input_pdf_name", help="The name of the input PDF file")

    parser.add_argument(
        "-o", "--output",
        dest="output_pdf_name",
        help="The name for the PDF output file",
        required=False,
    )

    input_parameters, unknown_input_parameters = parser.parse_known_args()

    name = input_parameters.input_pdf_name
    output_name = output_name = name + "-output"
    if input_parameters.output_pdf_name is not None:
        output_name = input_parameters.output_pdf_name


    reader = PdfReader(name)
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)


    with open("{}".format(output_name), "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    main()