from gmpy2 import const_pi, context, get_context

with context(get_context(), precision = 128):
    PI = const_pi()
    HALF_PI = PI / 2
    TWO_PI = PI * 2
