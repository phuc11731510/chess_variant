"""Variant specification module (skeleton).

This module defines OOP skeletons for variant-related concepts. The
classes carry signatures and documentation only; implementations will be
added incrementally to preserve small, reviewable changes and SOLID design.
"""

from pathlib import Path


class PieceSpec:
  """Describes a piece type used in a chess variant.

  This class is a data model skeleton. It captures identification fields
  only at this stage; movement semantics and flags will be added later.
  """

  def __init__(self, key: str, name: str | None = None) -> None:
    """Initialize a piece specification.

    Parameters
    ----------
    key: str
      Unique piece key/symbol (e.g., "K", "Q", "p").
    name: str | None
      Optional human-readable name.
    """
    self.key = key
    self.name = name
    self.is_royal = False
    self.is_pawn_like = False
