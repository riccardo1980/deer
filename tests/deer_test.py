import pytest
import deer.preprocessing as prep


@pytest.mark.parametrize(
    "test_input, expected, expected_msg",
    [
        ('tests/data/check_format/ok/test1.txt', 'VALID', ''),
        ('tests/data/check_format/error/ISO-8859_CRLF_NEL.txt',
         'INVALID', 'not a valid format'),
        ('tests/data/check_format/error/UTF-8_LF.txt',
         'INVALID', 'not a valid terminator'),
        ('tests/data/check_format/error/UTF-8_LF_NEL.txt',
         'INVALID', 'not a valid terminator')
    ]
)
def test_eval(test_input, expected, expected_msg):
    try:
        prep.check_dataset(test_input)
    except AssertionError as e:
        result = 'INVALID'
        msg = str(e)
    else:
        result = 'VALID'
        msg = ''
    assert result == expected
    assert msg == expected_msg
