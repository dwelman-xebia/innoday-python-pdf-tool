# innoday-python-pdf-tool
A PDF manipulation CLI tool created during an Xebia innovation day

To run:

python main.py PDF_NAME FLAGS

CLI Arguments:
    -o: [OPTIONAL] Output name of the processed PDF
    -c: [FLAG][OPTIONAL] Compress the PDF
    -ri: [FLAG][OPTIONAL] Remove images - Note: This seems pretty buggy and may corrupt the output PDF, use with caution
    -e: [OPTIONAL] Password for to use to encrypt the PDF