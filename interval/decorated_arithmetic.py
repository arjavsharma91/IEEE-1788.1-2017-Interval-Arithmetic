from .interval import Interval
from .arithmetic import add as bare_add, sub as bare_sub, mul as bare_mul, div as bare_div
from .decorations import Decoration, combine
from .decorated_interval import DecoratedInterval

def add(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._corerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.nai

  interval = bare_add(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)

  return DecoratedInterval(interval, dec)

def sub(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._corerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.nai

  interval = bare_sub(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)

  return DecoratedInterval(interval, dec)

def mul(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._corerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.nai

  interval = bare_mul(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)

  return DecoratedInterval(interval, dec)

def div(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.nai

  if y.interval.contains(0):
    interval = Interval.entire()
    dec = Decoration.TRV
    return DecoratedInterval(interval, dec)

  interval = bare_div(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)

  return DecoratedInterval(interval, dec)
  
