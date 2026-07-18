#Handling Precision and Numeric Inputs

To ensure the mathematical rigor and strict standard compliance of `decoint`, it is critical to understand how Python handles numeric types before they are passed into the interval engine.

## The String Input Recommendation

When defining intervals with decimal values, **it is highly recommended to pass values as strings rather than standard Python floats.**

```python
from decoint import Interval

# ❌ NOT RECOMMENDED: The float 1.1 is already imprecise before creating the interval
invalid = Interval(1.1, 2.1)

# ✅ RECOMMENDED: High-precision parsing preserves exact decimal intent
valid = Interval("1.1", "2.1")
