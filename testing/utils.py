import random
from gmpy2 import mpfr, context, get_context, RoundNearest
from intervals.interval import Interval
from intervals.decorations import Decoration
from intervals.decorated_interval import DecoratedInterval

def rand_number(low=-10, high=10):
    return mpfr(random.uniform(low, high))

def rand_interval_mixed():
    r = random.random()
    if r < 0.15:
        return Interval.empty()
    elif r < 0.30:
        return Interval.entire()
    elif r < 0.45:
        return Interval(-1, 1)
    elif r < 0.60:
        x = rand_number()
        return Interval(x, x)
    else:
        a, b = rand_number(), rand_number()
        return Interval(min(a, b), max(a, b))

def rand_decorated_interval_mixed():
    bare = rand_interval_mixed()
    if bare.is_empty:
        return DecoratedInterval(bare, Decoration.TRV)
    
    dec = random.choice([Decoration.COM, Decoration.DAC, Decoration.DEF])
    return DecoratedInterval(bare, dec)

def sample(x: Interval):
    if x.is_empty:
        raise ValueError("Cannot sample an empty interval")
    if x.lo == x.hi:
        return x.lo
        
    lo_val = -1000.0 if x.lo == mpfr('-inf') else float(x.lo)
    hi_val = 1000.0 if x.hi == mpfr('inf') else float(x.hi)
    
    rand_frac = mpfr(random.random())
    with context(get_context()) as ctx:
        ctx.round = RoundNearest
        return x.lo + rand_frac * (hi_val - lo_val)

def assert_contains(x: Interval, value):
    val_mpfr = mpfr(value)
    assert x.lo <= val_mpfr <= x.hi, f"Containment Leak: Value {val_mpfr} fell outside {x}"
