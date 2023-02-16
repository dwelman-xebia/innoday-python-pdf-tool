import sys

from pypdf import PdfReader, PdfWriter
from argparse import ArgumentParser

from commands.compress import compress_page
from commands.remove_images import remove_images
from commands.encryption import encrypt, decrypt
from commands.merge import merge
from commands.split import range_to_page_indices

import os

parser = ArgumentParser(description=__doc__)

def main(args) -> int:

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
    parser.add_argument(
        "-ri", "--remove_images",
        dest="should_remove_images",
        action="store_true"
    )
    parser.add_argument(
        "-e", "--encrypt",
        dest="encrypt_key",
        help="The key to be used to encrypt the PDF file",
        required=False,
    )
    parser.add_argument(
        "-d", "--decrypt",
        dest="decrypt_key",
        help="The key to be used to decrypt the PDF file",
        required=False,
    )
    parser.add_argument(
        "-m", "--merge",
        dest="merge_file",
        help='''The name of a file to be merged into the input file in the format FILE_NAME:POSITION:PAGES, POSITION can be excluded or set to -1 to append to the end, specific PAGES can be specified (e.g. 1,2,6-10)''',
        nargs="+",
        required=False,
    )

    parser.add_argument(
        "-p", "--pages",
        dest="pages",
        help="Extract pages (e.g. '2,3-6')",
        required=False,
    )

    input_parameters, _unknown_input_parameters = parser.parse_known_args(args)

    name = input_parameters.input_pdf_name
    output_name = output_name = name + "-output"

    if input_parameters.output_pdf_name:
        output_name = input_parameters.output_pdf_name

    should_compress = False
    if input_parameters.should_compress:
        should_compress = input_parameters.should_compress
        if should_compress is True:
            print("- Compression Enabled")
    
    should_remove_images = False
    if input_parameters.should_remove_images:
        should_remove_images = input_parameters.should_remove_images
        if should_remove_images is True:
            print("- Remove Images Enabled")

    encryption_key = ""
    should_encrypt = False
    if input_parameters.encrypt_key:
        encryption_key = input_parameters.encrypt_key
        should_encrypt = True
        print("- Encrypting with key: {}".format(encryption_key))

    decryption_key = ""
    should_decrypt = False
    if input_parameters.decrypt_key:
        decryption_key = input_parameters.decrypt_key
        should_decrypt = True
        print("- Decryptying with key: {}".format(decryption_key))

    merge_files = []
    if input_parameters.merge_file:
        for file in input_parameters.merge_file:
            x = file.split(':')
            print(x)
            file_name = x[0]
            if not file_name.endswith(".pdf"):
                print("{} must end with '.pdf' extension".format(file_name))
                return 1
            pos = -1
            if len(x) > 1:
                pos = int(x[1])
            pages = []
            if len(x) > 2:
                pages = list(range_to_page_indices(x[2]))
            print("- Merging file: {} {}".format(file_name, "at position {}".format(pos) if pos > -1 else ""))
            merge_files.append((file_name, pos, pages))
    
    page_range = None
    if input_parameters.pages:
        if merge_files:
            print("Selecting pages is incompatible with merging pages")
            return 1
        page_range = list(range_to_page_indices(input_parameters.pages))
        
    if not name.endswith(".pdf"):
        print("File must end with '.pdf' extension")
        return 1

    if not output_name.endswith(".pdf"):
        output_name += ".pdf"

    reader = PdfReader(name)

    if should_decrypt:
        if reader.is_encrypted:
            reader = decrypt(reader, decryption_key)

    input_file_stats = os.stat(name)
    print('''Input file stats:
        Size in bytes: {}
        Pages: {}
    '''.format(input_file_stats.st_size, len(reader.pages)))

    writer = PdfWriter()

    for index, page in enumerate(reader.pages):
        if page_range and index not in page_range:
            continue
        if should_compress:
            page = compress_page(page)
        writer.add_page(page)

    for file, pos, pages in merge_files:
        writer = merge(writer, file, pos, pages)

    if should_remove_images:
        writer = remove_images(writer)

    if should_encrypt:
        writer = encrypt(writer, encryption_key)

    with open("{}".format(output_name), "wb") as f:
        writer.write(f)

    output_file_stats = os.stat(output_name)
    print('''Input file stats:
        Size in bytes: {}
        Pages: {}
    '''.format(output_file_stats.st_size, len(writer.pages)))

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))