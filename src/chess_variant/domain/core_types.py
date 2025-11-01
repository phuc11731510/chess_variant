from enum import Enum
from dataclasses import dataclass


class Color(str, Enum):
  """Màu quân cờ.

  Kế thừa từ `str` và `Enum` để:
  - so sánh/ghi log/serialize như chuỗi ('W'/'B'),
  - vẫn đảm bảo tính an toàn kiểu và tập giá trị hữu hạn của Enum.
  """

  WHITE = 'W'
  BLACK = 'B'

  def opponent(self) -> 'Color':
    """Trả về màu đối phương (WHITE ↔ BLACK)."""
    return Color.BLACK if self is Color.WHITE else Color.WHITE

  def to_prefix(self) -> str:
    """Trả về tiền tố hiển thị cho màu: 'w' hoặc 'b'."""
    return 'w' if self is Color.WHITE else 'b'
  
@dataclass(frozen=True)
class Pos:
  """Tọa độ một ô trên bàn cờ.

  - x: chỉ số hàng (row), 0 ở trên cùng và tăng dần xuống dưới.
  - y: chỉ số cột (col), 0 ở bên trái và tăng dần sang phải.
  """

  x: int
  y: int

  def in_bounds(self, width: int, height: int) -> bool:
    """Kiểm tra tọa độ có nằm trong bàn cờ hay không.

    Tham số:
    - width: số cột của bàn cờ.
    - height: số hàng của bàn cờ.

    Ghi nhớ quy ước trục: x so với `height`, y so với `width`.
    Trả về True nếu (0 <= x < height) và (0 <= y < width).
    """
    return 0 <= self.x < height and 0 <= self.y < width


def algebraic_to_pos(text: str, height: int, width: int) -> Pos:
  """Chuyển ký hiệu đại số (ví dụ: 'a1', 'c3') thành `Pos`.

  Quy ước chuyển đổi theo hệ trục của dự án:
  - file (chữ cái) ánh xạ sang cột `y`, với 'a' → 0, 'b' → 1, ...
  - rank (số) ánh xạ sang hàng `x`, với rank 1 → x=0 (hàng trên cùng).

  Hỗ trợ kích thước bàn cờ tùy ý: `height` (số hàng) và `width` (số cột).
  Ném `ValueError` nếu tọa độ vượt biên hoặc định dạng không hợp lệ.
  """
  t = text.strip().lower()
  if len(t) < 2:
    raise ValueError('coordinate too short')
  file_ch = t[0]
  rank_str = t[1:]
  if not ('a' <= file_ch <= 'z'):
    raise ValueError('file must be a-z')
  if not rank_str.isdigit():
    raise ValueError('rank must be digits')
  y = ord(file_ch) - ord('a')
  if y < 0 or y >= width:
    raise ValueError('file out of bounds for board width')
  rank = int(rank_str)
  if rank < 1 or rank > height:
    raise ValueError('rank out of bounds for board height')
  x = rank - 1  # rank 1 là hàng trên cùng theo quy ước của dự án
  return Pos(x, y)


def pos_to_algebraic(pos: Pos, height: int, width: int) -> str:
  """Chuyển `Pos(x,y)` về ký hiệu đại số dạng 'a1'.

  Theo hệ trục dự án: cột `y` ánh xạ sang chữ cái (file), hàng `x` ánh xạ
  sang số (rank) với `rank = x + 1`. Hỗ trợ kiểm tra biên theo `height` và
  `width`. Chỉ hỗ trợ cột trong phạm vi a..z.

  Ném `ValueError` nếu `pos` nằm ngoài biên hoặc `y` vượt quá 'z'.
  """
  if not pos.in_bounds(width, height):
    raise ValueError('position out of bounds for board')
  if pos.y >= 26:
    raise ValueError('file beyond z is not supported')
  file_ch = chr(ord('a') + pos.y)
  rank = pos.x + 1
  return f"{file_ch}{rank}"


@dataclass(frozen=True)
class Move:
  """Nước đi cơ bản trong ván cờ.

  Thuộc tính:
  - src: ô xuất phát (`Pos`).
  - dst: ô đích (`Pos`).
  - promotion: mã quân phong cấp (ví dụ 'Q') hoặc None.
  """

  src: Pos
  dst: Pos
  promotion: str | None = None



if __name__ == '__main__':
  print(pos_to_algebraic(Pos(5,3),10,10))
