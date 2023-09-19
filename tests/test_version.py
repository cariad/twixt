from twixt import get_version


def test() -> None:
    assert get_version() == "0.0.0"
