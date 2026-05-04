from decimal import Decimal, getcontext

def greeting():
    print("You are reading main.py")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits.
    Uses the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits (int): Number of decimal places to calculate (default: 5)
    
    Returns:
        Decimal: Pi calculated to the specified precision
    """
    # Set precision higher than needed for accurate calculation
    getcontext().prec = digits + 10
    
    # Machin formula: pi = 16*arctan(1/5) - 4*arctan(1/239)
    # This converges faster and is more accurate
    
    def arctan(x, num_terms=500):
        """Calculate arctan using Taylor series"""
        getcontext().prec = digits + 10
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    one = Decimal(1)
    five = Decimal(5)
    two_three_nine = Decimal(239)
    
    pi = 4 * (4 * arctan(one / five) - arctan(one / two_three_nine))
    
    # Set precision back to requested digits and return
    getcontext().prec = digits + 2
    return +pi  # The unary + operator rounds to the current precision


if __name__ == "__main__":
    pi_value = calculate_pi(5)
    print(f"Pi to 5 digits: {pi_value}")