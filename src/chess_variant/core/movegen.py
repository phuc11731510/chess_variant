 
"""Move generation strategies (skeleton).

This module defines the `MovementStrategy` interface that concrete piece
strategies will implement to generate pseudo-legal moves for a piece at
given coordinates. Implementations will be added incrementally.
"""

from abc import ABC, abstractmethod

from .board import Board
from .types import Color, Move


class MovementStrategy(ABC):
  """Strategy interface for generating moves of a piece type.

  Implementations must not mutate game state. They should return
  pseudo-legal moves (not filtered for self-check) based on the current
  board/position information provided externally.
  """

  @abstractmethod
  def generate_moves(self, board: Board, x: int, y: int, color: Color) -> list[Move]:
    """Generate pseudo-legal moves for a piece at (x, y).

    Coordinates follow the project convention:
    - x increases from top to bottom (rows)
    - y increases from left to right (columns)

    Parameters
    ----------
    board: Board
      The board context to query size/occupancy when applicable.
    x: int
      Row index (0..height-1).
    y: int
      Column index (0..width-1).
    color: Color
      The color of the piece for color-dependent behavior.

    Returns
    -------
    list[Move]
      A list of pseudo-legal moves from (x, y).
    """
    raise NotImplementedError
