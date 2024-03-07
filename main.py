"""Sample example to test the package.

Created by @pytholic on 2024.02.25
"""

from stringutils.utils import (
    add_list_elements,
    capitalize_string,
    reverse_string,
)

if __name__ == "__main__":
    input_string = "Hello"
    print(capitalize_string(input_string))
    print(reverse_string(input_string))

    in1 = ["hello", "good"]
    in2 = ["hi", "bye"]
    print(add_list_elements(in1, in2))

    in1 = ["Big", "Good", "Light"]
    in2 = ["Small", "Bad", "Heavy"]
    print(add_list_elements(in1, in2))
