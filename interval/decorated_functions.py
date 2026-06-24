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
