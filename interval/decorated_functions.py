from .decorated_interval import DecoratedInterval
from .decorations import Decoration, combine
#Ill import the functions later cuz im stupid and lazy

def exp(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp(x.interval)
  dec = combine(x.decoration)
  return DecoratedInterval(interval, dec)

def sqrt(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 0:
    return DecoratedInterval.empty()
  elif x.interval.lo < 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_sqrt(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def log(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 0:
    return DecoratedInterval.empty()
  elif x.interval.lo < 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_log(x.interval)
  dec = combine(x.decoration, op_dec)
  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def pow_int(x, n):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if n < 0 and x.interval.contains(0):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_pow_int(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def sign(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.contains(0) and not x.interval.is_point:
    op_dec = Decoration.DEF
  else:
    op_dec = Decoration.COM

  interval = bare_sign(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_min(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_min(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_max(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_max(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def nth_root(x, n):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if n <= 0:
    raise ValueError("n must be positive")
  if n % 2 == 1:
    op_dec = Decoration.COM
  else:
    if x.interval.hi < 0:
      return DecoratedInterval.empty()
    elif x.interval.lo < 0:
      op_dec = Decoration.TRV
    else:
      op_dec = Decoration.COM
  interval = bare_nth_root(x.interval, n)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sin(x)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def cos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cos(x)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if bare_contains_periodic_point(x.interval, HALF_PI, PI):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_tan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def asin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_asin(x)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def asin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acos(x)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.is_nai()
  op_dec = Decoration.COM

  interval = bare_atan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def cosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_tanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)
  
def asinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_asinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def acosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi <= -1 or x.interval.lo >= 1:
    return DecoratedInterval.empty()
  elif x.interval.lo <= -1 or x.interval.hi >= 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_atanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def abs(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.lo >= 0:
    return Interval(x.lo, x.hi)
  elif x.hi <= 0:
    return Interval(-x.hi, -x.lo)

  hi = max(-x.lo, x.hi)
  return Interval(Number(0), hi)

def atan2(x, y):
  y = Interval._coerce(y)
  x = Interval._coerce(x)

  if y.is_empty or x.is_empty:
    return Interval.empty()

  if y.lo == 0 and y.hi == 0 and x.lo == 0 and x.hi == 0:
    return Interval.empty()

  if x.lo < 0 and y.lo < 0 and y.hi > 0:
    with context(get_context()) as ctx:
      ctx.round = RoundDown
      lo = -PI
    with context(get_context()) as ctx:
      ctx.round = RoundUp
      hi = PI
    return Interval(lo, hi)

  c1_lo, c1_up = atan2_down(y.lo, x.lo), atan2_up(y.lo, x.lo)
  c2_lo, c2_up = atan2_down(y.lo, x.hi), atan2_up(y.lo, x.hi)
  c3_lo, c3_hi = atan2_down(y.hi, x.lo), atan2_up(y.hi, x.lo)
  c4_lo, c4_hi = atan2_down(y.hi, x.hi), atan2_up(y.hi, x.hi)

  return Interval(min(c1_lo, c2_lo, c3_lo, c4_lo), max(c1_hi, c2_hi, c3_hi, c4_hi))
