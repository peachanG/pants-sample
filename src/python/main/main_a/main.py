from lib.lib_a.utils.array import get_zero_array
from lib.lib_a.utils.log import set_logging_basic_config
from python.lib.lib_a.utils.array import get_zero_tf_array


if __name__ == "__main__":
    set_logging_basic_config("INFO")
    print(get_zero_array([1, 2, 3]))
    print(get_zero_tf_array([1, 2, 3]))
