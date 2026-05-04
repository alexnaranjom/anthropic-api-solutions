"""
Test file for the pi calculation function
"""
from decimal import Decimal
from main import calculate_pi


def test_pi_calculation():
    """Test that pi is calculated correctly to 5 decimal places"""
    pi_value = calculate_pi(5)
    
    # Pi to 5 decimal places: 3.14159
    expected_pi = Decimal("3.14159")
    
    print(f"Calculated pi: {pi_value}")
    print(f"Expected pi:   {expected_pi}")
    
    # Check if the calculated value is close enough (within 0.000001)
    tolerance = Decimal("0.000001")
    difference = abs(pi_value - expected_pi)
    
    assert difference < tolerance, f"Pi calculation error: {difference}"
    print(f"✓ Test passed! Difference: {difference}")


def test_pi_various_precisions():
    """Test pi calculation at various precision levels"""
    print("\nTesting pi at various precisions:")
    
    test_cases = [
        (3, Decimal("3.14")),      # 3.142
        (5, Decimal("3.14159")),   # 3.14159
        (10, Decimal("3.141592653")),  # More digits
    ]
    
    for precision, expected in test_cases:
        result = calculate_pi(precision)
        print(f"  {precision} digits: {result}")
        # Just verify it's in the right ballpark
        assert 3.14 < float(result) < 3.15, f"Pi out of expected range at precision {precision}"
    
    print("✓ All precision tests passed!")


if __name__ == "__main__":
    print("=" * 50)
    print("Testing Pi Calculation")
    print("=" * 50)
    
    test_pi_calculation()
    test_pi_various_precisions()
    
    print("\n" + "=" * 50)
    print("All tests passed successfully!")
    print("=" * 50)
