def square(x):
    """Returns the square of a number, or 'Invalid Input' for non-numeric types."""
    if isinstance(x, (int, float)):
        return x * x
    return "Invalid Input"

def get_test_cases():
    return [
        {"input": 2, "expected": 4},
        {"input": -3, "expected": 9},
        {"input": 0, "expected": 0},
        {"input": 5, "expected": 25},
        {"input": 10, "expected": 100},
        {"input": -1, "expected": 1},
        {"input": 3.5, "expected": 12.25},
        {"input": "text", "expected": "Invalid Input"},
    ]

def run_tests():
    print("=" * 50)
    print(" Automated Software Testing: square(x) ".center(50, "="))
    print("=" * 50)
    test_cases = get_test_cases()
    passed = 0

    print(f"{'Test':<6}{'Input':<10}{'Expected':<15}{'Actual':<15}{'Result'}")
    print("-" * 50)
    for idx, test in enumerate(test_cases, 1):
        inp = test["input"]
        expected = test["expected"]
        actual = square(inp)
        result = "PASS" if actual == expected else "FAIL"
        if result == "PASS":
            passed += 1
        print(f"{idx:<6}{repr(inp):<10}{repr(expected):<15}{repr(actual):<15}{result}")

    print("-" * 50)
    print()
    print(f"Summary: {passed}/{len(test_cases)} tests passed.")
    print("=" * 50)

if __name__ == "__main__":
    run_tests()
