from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .board import Board
  from .core_types import Pos, Move


class Piece(ABC):
  """Lớp cơ sở trừu tượng cho mọi quân cờ.

  Mục tiêu: cung cấp giao diện thống nhất cho việc sinh nước đi
  hợp lệ theo trạng thái bàn cờ. Các lớp quân cụ thể (Vua, Hậu,
  Xe, Tượng, Mã, Tốt, v.v.) sẽ kế thừa và hiện thực phương thức
  sinh nước đi tương ứng.
  """

  @abstractmethod
  def legal_moves(self, board: Board) -> list[Move]:
    """Trả về danh sách nước đi hợp lệ dạng `Move`.

    Tham số:
    - board: trạng thái bàn cờ hiện tại (được dùng để kiểm tra biên,
      va chạm, và các ràng buộc luật khác).
    """
    raise NotImplementedError
