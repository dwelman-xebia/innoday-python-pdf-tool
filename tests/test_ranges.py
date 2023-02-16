from commands.split import range_to_page_indices

def test_one_page():
    indices = list(range_to_page_indices("5"))

    assert indices == [4]

def test_two_pages():
    indices = list(range_to_page_indices("3,5"))

    assert indices == [2,4]


def test_page_range():
    indices = list(range_to_page_indices("3-5"))

    assert indices == [2,3,4]

