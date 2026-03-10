from decimal import Decimal, getcontext

# Example calculation with higher precision
getcontext().prec = 28  # Use higher precision for internal calculation
result = Decimal('1') / Decimal('7')

# Format the output string to exactly 7 decimal places
print(f"Formatted result: {result:.7f}")
# Example output: Formatted result: 0.1428571
