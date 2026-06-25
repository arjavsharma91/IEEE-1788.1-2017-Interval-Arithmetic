from tests.utils import rand_interval_mixed, sample, assert_contains

def run_property_fuzzer(trials=1000):
    """Fuzzes operations dynamically using property-based containment verification."""
    for _ in range(trials):
        x = rand_interval_mixed()
        y = rand_interval_mixed()
        
        # Invariant 1: Structural Sanity
        assert x.lo <= x.hi or x.is_empty
        if x.is_empty:
            assert x.lo > x.hi
        
        # Invariant 2: Operational Point Containment
        if not x.is_empty and not y.is_empty:
            a = sample(x)
            b = sample(y)
            
            assert_contains(x + y, a + b)
            assert_contains(x - y, a - b)
            assert_contains(x * y, a * b)
            
            if not y.contains(0):
                assert_contains(x / y, a / b)

    print(f"✅ Passed {trials} random property fuzzer loops successfully.")
