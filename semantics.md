SEMANTICS

Empty intervals are represented as [+∞, -∞]
For all arithmetic operations, empty op x = empty
empty overlaps x = False
empty contains x = False
empty precedes x = False
empty meets x = False
empty ⊆ x = True
Undefined scalar quantities on empty intervals return NaN:
  -midpoint
  -width
  -radius
  -magnitude
  -mignitude
Division by intervals containing zero returns the entire interval as a conservative enclosure because disconnected interval unions are not currently represented.
