from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from ..domain.board import Board


def render(board: 'Board') -> str:
  """Kết xuất bàn cờ dạng ASCII dựa trên `board.squares`.

  Quy ước hiển thị:
  - Cột ghi bằng chữ: a.. (đến bề rộng bàn).
  - Hàng ghi bằng số: 1.. (hàng 1 ở trên cùng, phù hợp hệ trục x).
  - Ô trống: '.'
  - Ô có quân: ký tự đầu của tên lớp quân (P, N, B, R, Q, K, ...);
    chữ hoa cho quân Trắng, chữ thường cho quân Đen. Nếu không xác định
    được màu, dùng '?'.
  """
  width = board.width
  height = board.height
  header = '   ' + ' '.join([chr(ord('a') + i) for i in range(width)])
  lines = [header]
  for x in range(height):
    row_cells = []
    for y in range(width):
      sq = board.squares[x][y]
      p = sq.piece
      if p is None:
        row_cells.append('.')
      else:
        initial = p.__class__.__name__[0] if p.__class__.__name__ else '?'
        col = getattr(p, 'color', None)
        try:
          val = str(col)
        except Exception:
          val = ''
        ch = initial.upper() if val == 'W' else (initial.lower() if val == 'B' else '?')
        row_cells.append(ch)
    lines.append(f"{x+1:>2} " + ' '.join(row_cells))
  return '\n'.join(lines)

