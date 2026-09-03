from src.pomodoro import countdown


def test_countdown_zero_minutes():
    result = countdown(0, "Test")

    assert result is None
