# %%
from pypdf import PdfReader, PdfWriter
from pathlib import Path

# %%

black_hack = PdfReader(Path("The_Black_Hack_2e_PDF_2.2.pdf"))
len(black_hack.pages)

# %%
part = PdfWriter()

for p in black_hack.pages[0:15]:
    part.add_page(p)

part.write("part-pdf.pdf")
part.close()