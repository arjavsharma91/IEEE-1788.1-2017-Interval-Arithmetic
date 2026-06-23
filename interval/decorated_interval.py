from .interval import Interval
from dataclasses import dataclass
from .decorations import Decoration

@dataclass(frozen=True)
class DecoratedInterval:
  interval: Interval
  decoration: Decoration
  nai: bool = False
  def __post_init__(self):
    if not isinstance(self.interval, Interval):
      raise TypeError("Expected Interval")

    if not isinstance(self.decoration, Decoration):
      raise TypeError("Expected Decoration")

    if self.nai:
      if self.decoration != Decoration.ILL:
        raise ValueError("NaI must have decoration ILL")
  
  @classmethod
  def empty(cls):
    return cls(Interval.empty(), Decoration.TRV)
  
  @classmethod
  def entire(cls):
    return cls(Interval.entire(), Decoration.TRV

  @classmethod
  def nai(cls):
    return cls(Interval.empty(), Decoration.ILL, nai = True)

  def _coerce(cls, value):
    if isinstance(value, cls):
      return value

    if isinstance(value, Interval):
      if value.is_empty:
        dec = Decoration.TRV
      elif value.is_bounded:
        dec = Decoration.COM
      else:
        dec = Decoration.DAC

      return cls(value, dec)

    return cls._coerce(Interval._coerce(value))
