A simple Python guessing game using the `random` module.
The game generates a random number between 1 and 50 and continues until the player guesses the correct number.

## Features

- "Too low" / "Too high" hints after each guess
- Counts valid guesses and shows the total on a win
- Handles bad input without crashing:
  - Letters, decimals, or empty input ask for a valid number
  - Numbers outside 1-50 are rejected with a clear message

## Edge cases I tested

| Input | Result |
|---|---|
| abc | Please enter a valid number. |
| (empty, just Enter) | Please enter a valid number. |
| 5.5 | Please enter a valid number. |
| 0 or 51 | Number must be between 1 and 50. |
| Correct number | Win message with guess count |


## Concepts Practiced
- Python modules
- Functions
- `while` loop
- `if`, `elif`, `else`
- `break` statement
- User input
- Error handling with `try/except`
- Input validation and testing edge cases

## Output
I have uploaded a screenshot of my game output to this repository.