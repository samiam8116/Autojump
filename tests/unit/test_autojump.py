import os

from autojump_data import dictify, entriefy

ifilter = filter


def purge_missing_paths(entries):
    """Remove non-existent paths from a list of entries."""
    def f(entry):
        exists = os.path.exists(entry.path)
        return exists
    return ifilter(f, entries)


def test_purge_missing_paths():
    data_one = {'foo/bar': 0}
    data_two = {'foo/bar': 0,
                'foo/bar/bar': 1}
    data_exists = os.getcwd()
    data_three = {data_exists: 0}
    data_four = {data_exists: 0,
                 'foo/bar': 1}
    new_data_one = dictify(purge_missing_paths(entriefy(data_one)))
    new_data_two = dictify(purge_missing_paths(entriefy(data_two)))
    new_data_three = dictify(purge_missing_paths(entriefy(data_three)))
    new_data_four = dictify(purge_missing_paths(entriefy(data_four)))
    assert (len(data_one) - len(new_data_one)) == 1
    assert (len(data_two) - len(new_data_two)) == 2
    assert (len(data_three) - len(new_data_three)) == 0
    assert (len(data_four) - len(new_data_four)) == 1
