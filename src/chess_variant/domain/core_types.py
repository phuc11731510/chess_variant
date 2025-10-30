from enum import Enum
from dataclasses import dataclass


class Color(str, Enum):
  WHITE = 'W'
  BLACK = 'B'


if __name__ == '__main__':
  w = Color.WHITE
  b = Color.BLACK
  
  print('members:', w, b)
  print('names:', w.name, b.name)
  print('values:', w.value, b.value)

  print('isinstance(Color.WHITE, Color):', isinstance(w, Color))
  print('isinstance(Color.WHITE, str):', isinstance(w, str))

  print("w == 'W':", w == 'W')
  print('w == b:', w == b)

  # d = {'W': 'white', 'B': 'black'}
  # print("dict['W'] via enum key:", d[w])

  # s = {w, 'W'}
  # print('set dedupe with str value (size):', len(s))

  # print('constructor gives same identity:', w is Color('W'))


@dataclass(frozen=True)
class Pos:
  x: int
  y: int

  def in_bounds(self, width: int, height: int) -> bool:
    return 0 <= self.x < width and 0 <= self.y < height
