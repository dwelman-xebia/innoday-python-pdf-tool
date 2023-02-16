

def test_one_page():
    indices = list(range_to_page_indices("5"))

    assert indices == [4]

def test_two_pages():
    indices = list(range_to_page_indices("3,5"))

    assert indices == [2,4]


def test_page_range():
    indices = list(range_to_page_indices("3-5"))

    assert indices == [2,3,4]


def range_to_page_indices(page_numbers):
    for pn in page_numbers.split(","):
        if "-" in pn:
            f, t = pn.split("-")
            yield from range(int(f.strip()) - 1, int(t.strip()))
        else:
            yield int(pn.strip()) - 1
