from PIL import Image, ImageDraw
from pytest import mark, raises
from vecked import Region2f, Vector2f

from twixt import Track


def test_draw__incomplete() -> None:
    image = Image.new(
        "RGB",
        (1, 1),
        (255, 255, 255),
    )

    draw = ImageDraw.Draw(image)
    track = Track("x")

    with raises(ValueError) as ex:
        track.draw(draw, Region2f(Vector2f(0, 0), Vector2f(0, 0)))

    assert str(ex.value) == "Cannot render an incomplete track"


def test_draw__not_draw() -> None:
    track = Track("x")
    with raises(TypeError) as ex:
        track.draw("pizza", Region2f(Vector2f(0, 0), Vector2f(0, 0)))

    assert str(ex.value) == "image_draw is not PIL.ImageDraw"


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
