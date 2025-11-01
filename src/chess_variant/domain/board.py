from __future__ import annotations

try:
  from .core_types import Pos, Color, algebraic_to_pos, pos_to_algebraic as _pos_to_alg
except Exception:
  import sys
  from pathlib import Path
  SRC_DIR = Path(__file__).resolve().parents[2]
  if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
  from chess_variant.domain.core_types import Pos, Color, algebraic_to_pos, pos_to_algebraic as _pos_to_alg

from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .piece import Piece


class Square:
  """Ô vuông trên bàn cờ, tự quản lý tọa độ và quân cờ của mình.

  Thuộc tính:
  - pos: tọa độ `Pos` (x: hàng, y: cột).
  - piece: quân cờ đứng trên ô (có thể không có).
  """

  def __init__(self, pos: Pos) -> None:
    """Khởi tạo ô với tọa độ `pos` và trạng thái trống (piece=None)."""
    self.pos = pos
    self.piece: 'Piece | None' = None

  def __repr__(self) -> str:
    """Chuỗi hiển thị ngắn của ô.

    - Có quân: ủy quyền cho quân cờ tự cung cấp ký hiệu qua `Piece.symbol()`
      để tuân thủ SOLID (trách nhiệm thuộc về lớp quân).
    - Không có quân: in "..".
    """
    p = self.piece
    if p is None:
      return ".."
    return p.symbol()


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
    # Ma trận ô vuông, mỗi ô tự biết tọa độ của mình và chứa 0 hoặc 1 quân cờ
    self.squares: list[list[Square]] = []
    for x in range(self.height):
      row: list[Square] = []
      for y in range(self.width):
        row.append(Square(Pos(x, y)))
      self.squares.append(row)

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
    """Cho biết ô `pos` có trống không dựa trên `squares`."""
    return self.squares[pos.x][pos.y].piece is None

  def place(self, piece: 'Piece') -> None:
    """Đặt quân cờ vào ô tương ứng trong `squares`."""
    self.squares[piece.pos.x][piece.pos.y].piece = piece

  def iter_pieces(self) -> 'list[Piece]':
    """Trả về danh sách tất cả quân cờ đang có trên bàn.

    Duyệt qua lưới `squares` và gom các `piece` khác None.
    """
    result: 'list[Piece]' = []
    for x in range(self.height):
      for y in range(self.width):
        p = self.squares[x][y].piece
        if p is not None:
          result.append(p)
    return result
  
  def get(self, pos: Pos) -> 'Piece | None':
    """Trả về quân cờ tại ô `pos`, hoặc None nếu ô trống."""
    return self.squares[pos.x][pos.y].piece

  def remove(self, pos: Pos) -> None:
    """Xóa quân cờ tại ô `pos` (nếu có), biến ô thành trống."""
    self.squares[pos.x][pos.y].piece = None

  def clear(self) -> None:
    """Xóa toàn bộ quân cờ trên bàn, đưa tất cả ô về trạng thái trống."""
    for x in range(self.height):
      for y in range(self.width):
        self.squares[x][y].piece = None


if __name__ == '__main__':
  pass
