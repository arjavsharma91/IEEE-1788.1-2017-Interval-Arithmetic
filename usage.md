# Initialization Guide: Creating Intervals and Decorated Intervals

`decoint` provides two primary types for interval arithmetic: `Interval` (for standard mathematical intervals) and `DecoratedInterval` (which attaches a decoration state to track the validity of operations over domains, as defined by the IEEE 1788.1-2017 standard).

To ensure full mathematical rigor, always prefer passing numeric values as strings where applicable to prevent Python from introducing rounding errors prior to interval construction[cite: 1].

---

## 1. Basic `Interval` Initialization

A standard interval represents a closed, connected set of real numbers $[a, b]$. You can define them by passing the lower and upper bounds independently.

```python
from decoint import Interval

# Initialize using exact decimal string literals (Highly Recommended)
a = Interval("-1.5", "2.3")

# Initialize using exact integers or binary-exact floats
b = Interval(1, 5)          # [1, 5]
c = Interval("0.5")         # A point interval: [0.5, 0.5]

Handling Precision and Numeric Inputs

To ensure the mathematical rigor and strict standard compliance of `decoint`, it is critical to understand how Python handles numeric types before they are passed into the interval engine.

## The String Input Recommendation

When defining intervals with decimal values, **it is highly recommended to pass values as strings rather than standard Python floats.**

```python
from decoint import Interval

# ❌ NOT RECOMMENDED: The float 1.1 is already imprecise before creating the interval
invalid = Interval(1.1, 2.1)

# ✅ RECOMMENDED: High-precision parsing preserves exact decimal intent
valid = Interval("1.1", "2.1")
