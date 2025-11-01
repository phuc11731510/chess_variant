from __future__ import annotations

# Hỗ trợ chạy trực tiếp file này bằng Python (không qua gói)
try:
  from ..piece import Piece
  from ..board import Board
  from ..core_types import Pos, Move, Color
except Exception:
  import sys
  from pathlib import Path
  SRC_DIR = Path(__file__).resolve().parents[3]
  if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
  from chess_variant.domain.piece import Piece  # type: ignore
  from chess_variant.domain.board import Board  # type: ignore
  from chess_variant.domain.core_types import Pos, Move, Color  # type: ignore


class Pawn(Piece):
  """Quân Tốt với nước đi tối thiểu: tiến thẳng 1 ô.

  Ghi chú:
  - Cần có thuộc tính `self.pos` (Pos) và `self.color` (Color hoặc 'W'/'B').
  - Hướng di chuyển: trắng +1 theo trục x; đen −1 theo trục x.
  - Tuân thủ quy tắc: không dùng getattr()/callable(); không kiểm tra ô đích trống
    ở giai đoạn này (sẽ được xử lý bởi luật/board sau).
  """

  def legal_moves(self, board: Board) -> list[Move]:
    """Trả về các nước đi tiến thẳng 1 ô nếu còn trong biên bàn cờ.

    - Kiểm tra biên bằng `board.in_bounds`.
    - Không kiểm tra va chạm/ô trống ở đây.
    """
    pass
