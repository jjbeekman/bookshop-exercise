def is_valid_cin(cin: str) -> bool:
    """
    Checks if a 14 digit CIN is valid

    The assignment is to make this function return a boolean,
    but the better practice would be to raise exceptions
    so we can later catch them on any desired level.

    TODO: Change function signature to raise exception or return None
        .
        Reasoning from Stack Overflow (https://stackoverflow.com/questions/4670987/why-is-it-better-to-throw-an-exception-rather-than-return-an-error-code)
        1. Exceptions leaves your code clean of all the checks necessary when testing status returns on every call,
        2. Exceptions let you use the return value of functions for actual values,
        3. Exceptions can carry more information than a status return can,
        4. Most importantly: exceptions can't be ignored through inaction, while status returns can.
    """
    if len(cin) != 14 or not cin.isdigit():
        print("To compute the checksum, take the first 12 digits of the CIN")
        return False

    cin_partial = cin[:12]
    checksum = get_checksum(cin_partial)
    if checksum == cin[12:]:
        return True
    else:
        return False


def get_checksum(cin_partial: str) -> str:
    """
    Get the 2 digit checksum, using the first 12 digits of a CIN
    """
    if len(cin_partial) != 12 or not cin_partial.isdigit():
        raise AssertionError("To compute the checksum, supply the first 12 digits of the CIN")

    product = sum([int(n) * (m + 1) for m, n in enumerate(cin_partial)])
    checksum = str(product % 97)

    return checksum.zfill(2)  # zfill adds leading zero
