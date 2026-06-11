from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_numeric_comparison_bug_fix():
    """
    Test that numeric comparison is always used, not string comparison.
    This tests the bug fix: guesses should be compared numerically, not as strings.
    
    Example: secret=16, guess=12
    - Numeric: 12 < 16 → "Too Low" ✓
    - String: "12" > "16" lexicographically → "Too High" ✗ (BUG)
    """
    # Single digit vs double digit: "9" > "10" in string comparison
    assert check_guess(9, 10) == "Too Low"  # 9 < 10 numerically
    
    # Two digit edge case: "12" > "16" in string comparison, but 12 < 16 numerically
    assert check_guess(12, 16) == "Too Low"  # 12 < 16 (correct numeric comparison)


# parse_guess tests
def test_parse_guess_valid_number():
    """Test that valid numbers are parsed correctly."""
    ok, guess_int, err = parse_guess("50", 1, 100)
    assert ok == True
    assert guess_int == 50
    assert err == None

def test_parse_guess_float_to_int():
    """Test that decimal numbers are converted to integers."""
    ok, guess_int, err = parse_guess("50.7", 1, 100)
    assert ok == True
    assert guess_int == 50
    assert err == None

def test_parse_guess_empty_string():
    """Test that empty input returns an error."""
    ok, guess_int, err = parse_guess("", 1, 100)
    assert ok == False
    assert guess_int == None
    assert err == "Enter a guess."

def test_parse_guess_none():
    """Test that None input returns an error."""
    ok, guess_int, err = parse_guess(None, 1, 100)
    assert ok == False
    assert guess_int == None
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    """Test that non-numeric input returns an error."""
    ok, guess_int, err = parse_guess("abc", 1, 100)
    assert ok == False
    assert guess_int == None
    assert err == "That is not a number."

def test_parse_guess_out_of_range_too_low():
    """Test that guesses below the minimum are rejected."""
    ok, guess_int, err = parse_guess("5", 10, 50)
    assert ok == False
    assert guess_int == None
    assert "between 10 and 50" in err

def test_parse_guess_out_of_range_too_high():
    """Test that guesses above the maximum are rejected."""
    ok, guess_int, err = parse_guess("60", 10, 50)
    assert ok == False
    assert guess_int == None
    assert "between 10 and 50" in err

def test_parse_guess_within_easy_range():
    """Test valid guess within Easy difficulty range (1-20)."""
    ok, guess_int, err = parse_guess("15", 1, 20)
    assert ok == True
    assert guess_int == 15
    assert err == None

def test_parse_guess_within_hard_range():
    """Test valid guess within Hard difficulty range (1-100)."""
    ok, guess_int, err = parse_guess("75", 1, 100)
    assert ok == True
    assert guess_int == 75
    assert err == None
