import pytest


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonso",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


@pytest.mark.skip
def test_always_passes():
    assert True


@pytest.mark.xfail
def test_always_fails():
    assert False


def test_uppercase():
    assert "hello".upper() == 'HELLO'


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }


def format_data_for_display(people):
    formatted_data = []
    for person in people:
        info_string = f"{person['given_name']} {person['family_name']}: {person['title']}"
        formatted_data.append(info_string)
    return formatted_data


def format_data_for_excel(people):
    formatted_data = "given,family,title"
    for person in people:
        info_string = f"\n{person['given_name']},{person['family_name']},{person['title']}"
        formatted_data += info_string
    return formatted_data


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonso Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonso,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager"""


def is_palindrome(test_str):
    if test_str == reversed(test_str):
        return True
    return False


@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])


def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
