import os

import noxious
import pytest


@pytest.fixture()
def books():
    return noxious.from_file(open(os.path.join(os.path.dirname(__file__),
                                               'books.xml')))


def test_root(books):
    assert books._get_path() == "catalog"

    # should be only whitespace
    assert not str(books).strip()


def test_nonexistant(books):
    with pytest.raises(KeyError):
        books['steak']


def test_first_child(books):
    b1 = books['book']

    assert str(b1['genre']) == 'Computer'
    assert b1.id == 'bk101'
    assert repr(b1) == "catalog['book']"
    assert b1['genre'] + '-Book' == 'Computer-Book'
    assert 'Book: ' + b1['genre'] == 'Book: Computer'

    assert float(44.95) == float(b1['price'])

    with pytest.raises(ValueError):
        int(b1['price'])

    assert bool(b1) == True


def test_find_all_books(books):
    bs = books['book']._all()

    assert len(bs) == 12

    assert bs[3].id == 'bk104'
