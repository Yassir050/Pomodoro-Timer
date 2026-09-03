from src.pomodoro import countdown


def test_countdown():
    result = countdown(0, "Test")

    assert result is None
