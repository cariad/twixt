from pytest import mark, raises

from twixt import Transition
from twixt.functions import elastic, linear


@mark.parametrize(
    "transition, expect",
    [
        (
            Transition(
                0,
                9,
                linear(),
                10,
            ),
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
            Transition(
                0,
                9,
                elastic(),
                10,
            ),
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
def test_steps(
    transition: Transition,
    expect: list[float],
) -> None:
    assert list(transition.steps) == expect


def test_transition__range() -> None:
    with raises(ValueError) as ex:
        Transition(
            100,
            200,
            linear(),
            1,
        )

    assert str(ex.value) == "Transitions require at least two frames (1)"
