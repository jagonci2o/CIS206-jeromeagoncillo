import loopsBMI

# Test valid weight and height inputs
def test_userWeightAndHeight_validInput():
    input_values = [
        "150",  # Valid weight
        "5",    # Valid height in feet
        "10",   # Valid height in inches
        "c"     # Continue prompt
    ]
    
    def mock_input(prompt=None):
        return input_values.pop(0)

    loopsBMI.input = mock_input
    floWeight, floHeightTotal = loopsBMI.userWeightAndHeight()
    assert floWeight == 150, "Expected weight to be 150."
    assert floHeightTotal == (5 * 12) + 10, "Expected height in inches to be 70."

# Test BMI calculation with valid input
def test_calculateBMI_validInput():
    bmi = loopsBMI.calculateBMI(150, 70)
    assert round(bmi, 1) == 21.5, "Expected BMI to be 21.5."

# Test handling of invalid weight input
def test_userWeightAndHeight_invalidWeight():
    input_values = [
        "abc",  # Invalid weight
        "150",  # Valid weight after retry
        "5",    # Height in feet
        "10",   # Height in inches
        "c"     # Continue prompt
    ]
    
    def mock_input(prompt=None):
        return input_values.pop(0)

    loopsBMI.input = mock_input
    try:
        floWeight, floHeightTotal = loopsBMI.userWeightAndHeight()
        assert floWeight == 150, "Expected weight to be 150 after retry."
    except SystemExit:
        assert False, "Function should not exit on invalid input; it should retry."

# Test handling of invalid height in feet
def test_userWeightAndHeight_invalidHeightFt():
    input_values = [
        "150",  # Valid weight
        "xyz",  # Invalid height in feet
        "5",    # Valid height in feet after retry
        "10",   # Height in inches
        "c"     # Continue prompt
    ]

    def mock_input(prompt=None):
        return input_values.pop(0)

    loopsBMI.input = mock_input
    try:
        floWeight, floHeightTotal = loopsBMI.userWeightAndHeight()
        assert floHeightTotal == (5 * 12) + 10, "Expected height in inches to be 70 after retry."
    except SystemExit:
        assert False, "Function should not exit on invalid input; it should retry."

# Test handling of invalid height in inches
def test_userWeightAndHeight_invalidHeightIn():
    input_values = [
        "150",  # Valid weight
        "5",    # Height in feet
        "ten",  # Invalid height in inches
        "10",   # Valid height in inches after retry
        "c"     # Continue prompt
    ]

    def mock_input(prompt=None):
        return input_values.pop(0)

    loopsBMI.input = mock_input
    try:
        floWeight, floHeightTotal = loopsBMI.userWeightAndHeight()
        assert floHeightTotal == (5 * 12) + 10, "Expected height in inches to be 70 after retry."
    except SystemExit:
        assert False, "Function should not exit on invalid input; it should retry."

# Test BMI calculation when height is zero (should raise error)
def test_calculateBMI_zeroHeight():
    try:
        loopsBMI.calculateBMI(150, 0)  # Height cannot be zero
        assert False, "Function should raise an error for zero height."
    except ZeroDivisionError:
        pass  # Expected behavior

# Test BMI calculation when height is negative (should raise error)
def test_calculateBMI_negativeHeight():
    try:
        loopsBMI.calculateBMI(150, -70)  # Height cannot be negative
        assert False, "Function should raise an error for negative height."
    except ValueError:
        pass  # Expected behavior
