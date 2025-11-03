"""Board module: board representation interface (skeleton).

This module defines the public interface for the board representation.
Implementation will be added incrementally. The design follows SOLID by
keeping responsibilities focused (Board handles layout/state only).
"""

 


class Board:
  """Represents a game board for a chess variant.

  The board encapsulates only dimension and cell state responsibilities.
  Movement rules and validation will live in separate collaborators.
  """
  def __init__(self, height: int, width: int) -> None:
    """Initialize a board with explicit dimensions.

    Axis convention (from White's perspective):
    - x axis increases from top to bottom (rows)
    - y axis increases from left to right (columns)
    Therefore, `height` is the x-extent (row count), and `width` is the
    y-extent (column count). The coordinate (0, 0) is the top-left cell.
    """
    self.height = height
    self.width = width

  def get_size(self) -> tuple[int, int]:
    """Return the board size as (height, width)."""
    pass

  def is_in_bounds(self, x: int, y: int) -> bool:
    """Check whether coordinate (x, y) lies within the board bounds."""
    pass

  def clone(self) -> "Board":
    """Create a shallow copy of this board instance."""
    pass
