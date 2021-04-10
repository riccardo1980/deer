import codecs


def check_format(input_file: str):
    """
        Check for UTF-8 file
    """
    ret_value = True
    try:
        with codecs.open(input_file, 'r', 'utf-8') as input_stream:
            data = input_stream.read()  # noqa: F841
    except UnicodeDecodeError:
        ret_value = False
    assert ret_value, (
        'not a valid format'
    )


def check_newline(input_file: str):
    """
        Check for CRLF line termination on UTF-8 file
    """
    ret_value = True
    # universal line mode is enabled, but newline is returned untranslated
    with open(input_file, 'r', newline='') as input_stream:
        for line in input_stream:
            term = line[-2:]
            if term not in ['\r\n']:
                print('\t<{}>'.format(term.encode('utf-8')), end='')
                ret_value = False
                break
    assert ret_value, (
        'not a valid terminator'
    )


def check_dataset(input_file: str):
    """
        Check dataset file format
    """
    check_format(input_file)
    check_newline(input_file)
