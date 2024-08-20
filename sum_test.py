# tests/module1.py
from exercise import calcsum

def test_sum():
    result = calcsum.calculate_sum(5, 3)  # Assuming module2 has a calculate_sum function
    assert result == 8  # Your test assertion

if __name__ == "__main__":
    test_sum()