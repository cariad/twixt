from pytest import raises

from twixt import Composition, Transition


def test_add__exists(transition_up: Transition) -> None:
    composition = Composition[str]()

    composition.add("foo", transition_up)

    with raises(ValueError) as ex:
        composition.add("foo", transition_up)

    assert str(ex.value) == 'Transition "foo" already exists'


def test_steps(
    transition_up: Transition,
    transition_down: Transition,
) -> None:
    composition = Composition[str]()
    composition.add("up", transition_up)
    composition.add("down", transition_down)

    assert list(composition.steps) == [
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 36.666666666666664,
            "up": 90.0,
        },
        {
            "down": 33.333333333333336,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
    ]


def test_steps__lead_in(
    transition_up: Transition,
    transition_down: Transition,
) -> None:
    composition = Composition[str](lead_in=2)
    composition.add("up", transition_up)
    composition.add("down", transition_down)

    assert list(composition.steps) == [
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 36.666666666666664,
            "up": 90.0,
        },
        {
            "down": 33.333333333333336,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
    ]


def test_steps__lead_in_and_lead_out(
    transition_up: Transition,
    transition_down: Transition,
) -> None:
    composition = Composition[str](
        lead_in=2,
        lead_out=3,
    )

    composition.add("up", transition_up)
    composition.add("down", transition_down)

    assert list(composition.steps) == [
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 40,
            "up": 80,
        },
        {
            "down": 36.666666666666664,
            "up": 90.0,
        },
        {
            "down": 33.333333333333336,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
        {
            "down": 30.0,
            "up": 100.0,
        },
    ]
