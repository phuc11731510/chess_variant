"""Core value object types (skeleton).

This module defines minimal immutable-like value objects used across the
engine. These classes intentionally carry no behavior to keep concerns
separated and the design SOLID.
"""

from enum import Enum

class Coordinate:
  """Represents a board coordinate using zero-based indices.

  Attributes
  ----------
  x: int
    File index (0..width-1).
  y: int
    Rank index (0..height-1).
  """

  __slots__ = ("x", "y")

  def __init__(self, x: int, y: int) -> None:
    """Create a coordinate at (x, y)."""
    self.x = x
    self.y = y


class Move:
  """Represents a move from a source to a destination coordinate.

  Attributes
  ----------
  src: Coordinate
    Source coordinate.
  dst: Coordinate
    Destination coordinate.
  """

  __slots__ = ("src", "dst")

  def __init__(self, src: Coordinate, dst: Coordinate) -> None:
    """Create a move from `src` to `dst`."""
    self.src = src
    self.dst = dst


class Color(Enum):
  """Represents player color in the game.

  Provides two values: WHITE and BLACK. This enum carries no behavior
  to keep responsibilities minimal and aligned with SOLID.
  """

  WHITE = "white"
  BLACK = "black"
