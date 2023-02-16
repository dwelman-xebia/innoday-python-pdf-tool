# innoday-python-pdf-tool

A PDF manipulation CLI tool created during an Xebia innovation day

To run:

```bash
python -m pdftool PDF_NAME FLAGS
```

If you install pdftool with [Poetry](https://python-poetry.org/), you can install your app and run

```
pdftool -h
```

```
usage: pdftool [-h] [-o OUTPUT_PDF_NAME] [-c] [-ri] [-e ENCRYPT_KEY]
               [-d DECRYPT_KEY] [-m MERGE_FILE [MERGE_FILE ...]]
               [-p PAGES]
               input_pdf_name

positional arguments:
  input_pdf_name        The name of the input PDF file

options:
  -h, --help            show this help message and exit
  -o OUTPUT_PDF_NAME, --output OUTPUT_PDF_NAME
                        The name for the PDF output file
  -c, --compress
  -ri, --remove_images
  -e ENCRYPT_KEY, --encrypt ENCRYPT_KEY
                        The key to be used to encrypt the PDF file
  -d DECRYPT_KEY, --decrypt DECRYPT_KEY
                        The key to be used to decrypt the PDF file
  -m MERGE_FILE [MERGE_FILE ...], --merge MERGE_FILE [MERGE_FILE ...]
                        The name of a file to be merged into the input file in
                        the format FILE_NAME:POSITION:PAGES, POSITION can be
                        excluded or set to -1 to append to the end, specific
                        PAGES can be specified (e.g. 1,2,6-10)
  -p PAGES, --pages PAGES
                        Extract pages (e.g. '2,3-6')
```