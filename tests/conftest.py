from logging import DEBUG, getLogger

from pytest import fixture

from twixt import Transition, linear
from twixt.logging import logger

logger.setLevel(DEBUG)
getLogger("bendy").setLevel(DEBUG)


@fixture
def transition_down() -> Transition:
    return Transition(
        40,
        30,
        linear(),
        4,
    )


@fixture
def transition_up() -> Transition:
    return Transition(
        80,
        100,
        linear(),
        3,
    )
