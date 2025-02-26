from Serialization_file.json_to_py import deserialization_1, deserialization_2
from Serialization_file.py_to_json import serialization_1, serialization_2


def main():
    py_file=serialization_1()
    json_file=deserialization_1(py_file)
    py_file2=serialization_2()
    json_file2=deserialization_2(py_file2)

    print(json_file)
    print(py_file)
    print(py_file2)
    print(json_file2)
main()

