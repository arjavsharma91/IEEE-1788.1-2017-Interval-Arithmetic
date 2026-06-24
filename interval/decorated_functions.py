from .decorated_interval import DecoratedInterval
from .decorations import Decoration, combine
#Ill import the functions later cuz im stupid and lazy

def exp(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.nai
  interval = bare_exp(x.interval)
  dec = combine(x.decoration)
  return DecoratedInterval(interval, dec)

