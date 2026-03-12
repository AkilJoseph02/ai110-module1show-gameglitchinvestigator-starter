from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_get_range_difficulties():
    # ensure the corrected ranges are returned
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)
    # unknown difficulty should fall back to Normal
    assert get_range_for_difficulty("??") == (1, 50)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess():
    ok, val, err = parse_guess("")
    assert not ok and err
    ok, val, err = parse_guess("abc")
    assert not ok and err
    ok, val, err = parse_guess("5")
    assert ok and val == 5
    ok, val, err = parse_guess("3.0")
    assert ok and val == 3


def test_update_score():
    # winning early gives more points
    assert update_score(0, "Win", 0) > update_score(0, "Win", 5)
    # too high even attempts add points
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too High", 3) == 5
    # too low always subtracts
    assert update_score(20, "Too Low", 1) == 15
