# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose:** A number guessing game where players guess a secret number based on difficulty level (Easy: 1-20, Normal: 1-50, Hard: 1-100) and receive hints to find it.

- [x] **Detail which bugs you found:**
  1. Wrong hints due to secret being converted to string 
  2. Difficulty ranges were backwards (Normal and Hard swapped)
  3. Accepted guesses outside the valid range
  4. Displayed wrong range in the hint message
  5. "New Game" button didn't reset properly

- [x] **Explain what fixes you applied:**
  1. Removed string conversion that caused wrong comparisons
  2. Fixed ranges: Easy (1-20), Normal (1-50), Hard (1-100)
  3. Added range validation to `parse_guess()`
  4. Updated hint to show actual difficulty range
  5. Fixed "New Game" to reset all state and use correct range

## 📸 Demo Walkthrough

1. Select a difficulty level from the sidebar
2. Enter a guess within the shown range
3. Get an accurate hint (Too High/Too Low)
4. Try entering a number outside the range—it's rejected
5. Win by finding the secret number
6. Click "New Game" to start fresh

## 🧪 Test Results

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/sindhuja/codepath/ai110-module1show-gameglitchinvestigator-starte
r
plugins: anyio-4.14.0
collected 13 items                                                             

tests/test_game_logic.py::test_winning_guess PASSED                      [  7%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 15%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 23%]
tests/test_game_logic.py::test_numeric_comparison_bug_fix PASSED         [ 30%]
tests/test_game_logic.py::test_parse_guess_valid_number PASSED           [ 38%]
tests/test_game_logic.py::test_parse_guess_float_to_int PASSED           [ 46%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED           [ 53%]
tests/test_game_logic.py::test_parse_guess_none PASSED                   [ 61%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED            [ 69%]
tests/test_game_logic.py::test_parse_guess_out_of_range_too_low PASSED   [ 76%]
tests/test_game_logic.py::test_parse_guess_out_of_range_too_high PASSED  [ 84%]
tests/test_game_logic.py::test_parse_guess_within_easy_range PASSED      [ 92%]
tests/test_game_logic.py::test_parse_guess_within_hard_range PASSED      [100%]

============================== 13 passed in 0.02s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
