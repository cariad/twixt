from pytest import mark

from twixt import Track


@mark.parametrize(
    "track, expect",
    [
        (Track(1, 1, value=3), 3),
        (Track(1, 1, value=3, ease_in_force=1), 4),
        (Track(1, 1, value=3, ease_in_force=-1), 3),
        (Track(1, 1, value=3).add_point(1, 2), 3),
        (Track(1, 1, value=3).add_point(1, 4), 4),
        (Track(1, 1, value=3).add_point(1, 2, ease_out_force=4), 3),
        (Track(1, 1, value=3).add_point(1, 2, ease_out_force=-4), 6),
    ],
)
def test_max_anchor(track: Track[int], expect: float) -> None:
    assert track.max_anchor == expect


@mark.parametrize(
    "track, expect",
    [
        (Track(1, 1, value=3), 3),
        (Track(1, 1, value=3, ease_in_force=1), 3),
        (Track(1, 1, value=3, ease_in_force=-1), 2),
        (Track(1, 1, value=3).add_point(1, 2), 2),
        (Track(1, 1, value=3).add_point(1, 4), 3),
        (Track(1, 1, value=3).add_point(1, 2, ease_out_force=4), -2),
        (Track(1, 1, value=3).add_point(1, 2, ease_out_force=-4), 2),
    ],
)
def test_min_anchor(track: Track[int], expect: float) -> None:
    assert track.min_anchor == expect
