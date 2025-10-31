try:
  from .core_types import Pos, algebraic_to_pos, pos_to_algebraic as _pos_to_alg
except Exception:
  import sys
  from pathlib import Path
  SRC_DIR = Path(__file__).resolve().parents[2]
  if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
  from chess_variant.domain.core_types import Pos, algebraic_to_pos, pos_to_algebraic as _pos_to_alg


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

  def in_bounds(self, pos: Pos) -> bool:
    """Kiểm tra ô `pos` có nằm trong phạm vi bàn cờ.

    Sử dụng quy ước trục: x so với `height`, y so với `width`.
    """
    return pos.in_bounds(self.width, self.height)

  def pos_from_algebraic(self, text: str) -> Pos:
    """Chuyển chuỗi tọa độ đại số sang `Pos` theo kích thước bàn hiện tại.

    Ví dụ: 'a1', 'c3'. Tuân theo quy ước trục (x: hàng, y: cột).
    """
    return algebraic_to_pos(text, self.height, self.width)

  def pos_to_algebraic(self, pos: Pos) -> str:
    """Chuyển `Pos` hiện tại sang ký hiệu đại số theo kích thước bàn.

    Ví dụ: Pos(0,0) → 'a1' với quy ước trục của dự án.
    """
    return _pos_to_alg(pos, self.height, self.width)


if __name__ == '__main__':
  pass
