from pytest import mark, raises

from twixt import Transform, transition
from twixt.transformers import elastic, linear


@mark.parametrize(
    "start, end, count, transformation, expect",
    [
        (
            0,
            9,
            10,
            linear(),
            [
                0.0,
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0,
                7.0,
                8.0,
                9.0,
            ],
        ),
        (
            0,
            9,
            10,
            elastic(),
            [
                0,
                -0.568935451855562,
                0.296792535084546,
                1.7658587713684133,
                3.61419984973704,
                5.580246913580247,
                7.402431106287856,
                8.819183571249688,
                9.59715520679708,
                9,
            ],
        ),
    ],
)
def test_transition(
    start: float,
    end: float,
    count: int,
    transformation: Transform,
    expect: list[float],
) -> None:
    result = transition(
        start,
        end,
        count,
        transformation,
    )

    assert list(result) == expect


def test_transition__range() -> None:
    result = transition(
        100,
        200,
        1,
        linear(),
    )

    with raises(ValueError) as ex:
        list(result)

    assert str(ex.value) == "count (1) must be >= 2"
