from __future__ import annotations

try:
  from .core_types import Pos, algebraic_to_pos, pos_to_algebraic as _pos_to_alg
except Exception:
  import sys
  from pathlib import Path
  SRC_DIR = Path(__file__).resolve().parents[2]
  if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
  from chess_variant.domain.core_types import Pos, algebraic_to_pos, pos_to_algebraic as _pos_to_alg

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .piece import Piece

# Alias duy nhất cho lưới ô: ma trận Piece hoặc None
Grid = list[list['Piece | None']]


class Board:
  """Bàn cờ với kích thước linh hoạt.

  Thuộc tính:
  - height: số hàng của bàn cờ (trục x).
  - width: số cột của bàn cờ (trục y).
  """

  def __init__(self, height: int, width: int) -> None:
    """Khởi tạo bàn cờ với số hàng `height` và số cột `width`."""
    self.height = height
    self.width = width
    # Ma trận 2 chiều (x: hàng, y: cột) lưu quân hoặc None
    self.cells: 'Grid' = [[None for _ in range(self.width)] for _ in range(self.height)]

  def in_bounds(self, pos: Pos) -> bool:
    """Kiểm tra ô `pos` có nằm trong phạm vi bàn cờ.

    Sử dụng quy ước trục: x so với `height`, y so với `width`.
    """
    return pos.in_bounds(self.width, self.height)

  def pos_from_algebraic(self, text: str) -> Pos:
    """Chuyển ký hiệu đại số (ví dụ 'a1', 'c3') sang `Pos` theo kích thước bàn hiện tại."""
    return algebraic_to_pos(text, self.height, self.width)

  def pos_to_algebraic(self, pos: Pos) -> str:
    """Chuyển `Pos` hiện tại sang ký hiệu đại số theo kích thước bàn."""
    return _pos_to_alg(pos, self.height, self.width)

  def is_empty(self, pos: Pos) -> bool:
    """Cho biết ô `pos` có trống không dựa trên ma trận `cells`."""
    return self.cells[pos.x][pos.y] is None

  def place(self, piece: 'Piece') -> None:
    """Đặt một quân cờ vào ô ứng với `piece.pos` trong `cells`.

    Phương thức này chỉ cập nhật lưu trữ nội bộ; các kiểm tra hợp lệ sẽ bổ sung sau.
    """
    self.cells[piece.pos.x][piece.pos.y] = piece


if __name__ == '__main__':
  pass
