def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str, min_val: int, max_val: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # Check if empty
    if raw is None or raw == "":
        return (False, None, "Enter a guess.")
    
    # Try to parse as number
    try:
        guess_float = float(raw)
        guess_int = int(guess_float)
    except (ValueError, TypeError):
        return (False, None, "That is not a number.")
    
    # Check if in range
    if guess_int < min_val or guess_int > max_val:
        return (False, None, f"Please enter a number between {min_val} and {max_val}.")
    
    return (True, guess_int, None)


def check_guess(guess, secret):
    """
    Compare guess to secret and return outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
