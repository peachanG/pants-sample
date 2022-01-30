from lib.lib_a.sample import Sample


def test_make_zero_array():
    array = Sample().make_zero_array(5)
    assert array.shape[0] == 5
