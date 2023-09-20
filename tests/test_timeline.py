from twixt import ComposedStep, Timeline


def test_add_track() -> None:
    timeline = Timeline[str](10)
    track = timeline.add_track("x", 0, 0, 0, 0)
    assert track.key == "x"


def test_frames() -> None:
    assert Timeline[str](10).frames == 10


def test_steps() -> None:
    timeline = Timeline[str](10)
    timeline.add_track("x").add_point(9, 9)

    assert list(timeline.steps) == [
        ComposedStep(frame=0, progress={"x": 0}),
        ComposedStep(frame=1, progress={"x": 1}),
        ComposedStep(frame=2, progress={"x": 2}),
        ComposedStep(frame=3, progress={"x": 3}),
        ComposedStep(frame=4, progress={"x": 4}),
        ComposedStep(frame=5, progress={"x": 5}),
        ComposedStep(frame=6, progress={"x": 6}),
        ComposedStep(frame=7, progress={"x": 7}),
        ComposedStep(frame=8, progress={"x": 8}),
        ComposedStep(frame=9, progress={"x": 9}),
    ]


def test_steps__constant() -> None:
    timeline = Timeline[str](6)
    timeline.add_track("x", 3, 9)

    assert list(timeline.steps) == [
        ComposedStep(frame=0, progress={"x": 9}),
        ComposedStep(frame=1, progress={"x": 9}),
        ComposedStep(frame=2, progress={"x": 9}),
        ComposedStep(frame=3, progress={"x": 9}),
        ComposedStep(frame=4, progress={"x": 9}),
        ComposedStep(frame=5, progress={"x": 9}),
    ]


def test_steps__inner() -> None:
    timeline = Timeline[str](12)
    timeline.add_track("x", 1).add_point(10, 9)

    assert list(timeline.steps) == [
        ComposedStep(frame=0, progress={"x": 0}),
        ComposedStep(frame=1, progress={"x": 0}),
        ComposedStep(frame=2, progress={"x": 1}),
        # Curve solutions are estimates. Don't lose any sleep over it.
        ComposedStep(frame=3, progress={"x": 2.0000000000000004}),
        ComposedStep(frame=4, progress={"x": 3}),
        ComposedStep(frame=5, progress={"x": 4}),
        ComposedStep(frame=6, progress={"x": 5}),
        ComposedStep(frame=7, progress={"x": 6}),
        ComposedStep(frame=8, progress={"x": 7}),
        ComposedStep(frame=9, progress={"x": 8}),
        ComposedStep(frame=10, progress={"x": 9}),
        ComposedStep(frame=11, progress={"x": 9}),
    ]


def test_steps__multiple() -> None:
    timeline = Timeline[str](20)
    timeline.add_track("x", 1).add_point(10, 9).add_point(19, 0)

    assert list(timeline.steps) == [
        # Before the first point
        ComposedStep(frame=0, progress={"x": 0}),
        # First point starts
        ComposedStep(frame=1, progress={"x": 0}),
        ComposedStep(frame=2, progress={"x": 1}),
        ComposedStep(frame=3, progress={"x": 2.0000000000000004}),
        ComposedStep(frame=4, progress={"x": 3}),
        ComposedStep(frame=5, progress={"x": 4}),
        ComposedStep(frame=6, progress={"x": 5}),
        ComposedStep(frame=7, progress={"x": 6}),
        ComposedStep(frame=8, progress={"x": 7}),
        ComposedStep(frame=9, progress={"x": 8}),
        ComposedStep(frame=10, progress={"x": 9}),
        ComposedStep(frame=11, progress={"x": 8.000000000000004}),
        ComposedStep(frame=12, progress={"x": 6.9999999999999964}),
        ComposedStep(frame=13, progress={"x": 5.999999999999999}),
        ComposedStep(frame=14, progress={"x": 5.000000000000002}),
        ComposedStep(frame=15, progress={"x": 4}),
        ComposedStep(frame=16, progress={"x": 3}),
        ComposedStep(frame=17, progress={"x": 1.9999999999999998}),
        ComposedStep(frame=18, progress={"x": 1}),
        ComposedStep(frame=19, progress={"x": 0}),
    ]
