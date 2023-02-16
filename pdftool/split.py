

def range_to_page_indices(page_numbers):
    for pn in page_numbers.split(","):
        if "-" in pn:
            f, t = pn.split("-")
            yield from range(int(f.strip()) - 1, int(t.strip()))
        else:
            yield int(pn.strip()) - 1
