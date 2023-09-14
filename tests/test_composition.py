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
            "frame": 0,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 1,
            "progress": {
                "down": 36.666666666666664,
                "up": 90.0,
            },
        },
        {
            "frame": 2,
            "progress": {
                "down": 33.333333333333336,
                "up": 100.0,
            },
        },
        {
            "frame": 3,
            "progress": {
                "down": 30.0,
                "up": 100,
            },
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
            "frame": 0,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 1,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 2,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 3,
            "progress": {
                "down": 36.666666666666664,
                "up": 90.0,
            },
        },
        {
            "frame": 4,
            "progress": {
                "down": 33.333333333333336,
                "up": 100.0,
            },
        },
        {
            "frame": 5,
            "progress": {
                "down": 30.0,
                "up": 100,
            },
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
            "frame": 0,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 1,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 2,
            "progress": {
                "down": 40,
                "up": 80,
            },
        },
        {
            "frame": 3,
            "progress": {
                "down": 36.666666666666664,
                "up": 90.0,
            },
        },
        {
            "frame": 4,
            "progress": {
                "down": 33.333333333333336,
                "up": 100.0,
            },
        },
        {
            "frame": 5,
            "progress": {
                "down": 30.0,
                "up": 100,
            },
        },
        {
            "frame": 6,
            "progress": {
                "down": 30,
                "up": 100,
            },
        },
        {
            "frame": 7,
            "progress": {
                "down": 30,
                "up": 100,
            },
        },
        {
            "frame": 8,
            "progress": {
                "down": 30,
                "up": 100,
            },
        },
    ]
