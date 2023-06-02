from gendiff.gendiff import generate_diff


def test_json_comparation():
    path1 = "tests/fixtures/file1.json"
    path2 = "tests/fixtures/file2.json"
    result = open("tests/fixtures/test_json_comparation_result.txt").read()

    assert generate_diff(path1, path2) == result
