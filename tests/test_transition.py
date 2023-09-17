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
                -0.5942612549316327,
                0.21935860625821174,
                1.712632493483926,
                3.537417888497703,
                5.462582111502295,
                7.287367506516073,
                8.780641393741789,
                9.594261254931633,
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
